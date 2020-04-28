#pragma rtGlobals=1	// Use modern global access method.

macro burst_ADP()

//Insert file details:
variable startnumber = 1		//The first (lowest) trace number
variable startalign = 1			//The trace number with 50Hz stim
variable endnumber = 14		//The last (highest) trace number
string cellname = "nm20180226c4_0"
string suffix = "_3spikes"
variable removefile = -1

//Initializa variables
variable resultsrow = 0
variable filenumber
variable counter

string filename
string output_wave
string output_wave_aligned
string integrated

filename = cellname + "0" + num2str(startnumber) + suffix
NMFolderChange(filename)
make /O /N=100 burst_ADP_results
make /O /T /N=100 burst_ADP_results_legend

//Baseline & generate avg waves
filenumber = startnumber  //reset counter
do
		if(filenumber<10)
			filename = cellname + "0" + num2str(filenumber) + suffix
		else
			filename = cellname + num2str(filenumber) + suffix
		endif
	NMFolderChange(filename)
	NMBaselineWaves( 1 , 0 , 300 )
	NMWavesStats( 1 , 0 , 2 , 1 , 0 , 0 , 0 , 1 )
	filenumber += 1
		if(filenumber == removefile)
			filenumber +=1
		endif
while(filenumber <= endnumber)

filenumber = startnumber  //reset counter
filename = cellname + "0" + num2str(filenumber) + suffix
NMFolderChange(filename)

//Copy avg waves into a single file/folder; For each timepoint/ISI, align the traces to the last AP peak and subtract from the first (50Hz) trace
filenumber = startnumber //reset counter
do
	output_wave = "a" + num2str(filenumber)
	output_wave_aligned = "aligned" + num2str(filenumber)
		if(filenumber<10)
			filename = "::" + cellname + "0" + num2str(filenumber) + suffix +":Avg_RAll_A0"
		else
			filename = "::" + cellname + num2str(filenumber) + suffix+ ":Avg_RAll_A0"
		endif
	duplicate /O $filename, $output_wave
	findpeak /R=(400,405) $output_wave
	duplicate /O /R=(V_PeakLoc,800) $output_wave, $output_wave_aligned
		if (filenumber == startalign)
			duplicate /O $output_wave_aligned, aligned_start
		endif

	filenumber += 1
		if(filenumber == removefile)
			filenumber +=1
		endif
while(filenumber <= endnumber)

//Calculate integral
filenumber = startnumber
do
	$"aligned"+num2str(filenumber) -= aligned_start
	integrated = "integrated"+ num2str(filenumber)
	integrate $"aligned"+num2str(filenumber) /d=$integrated
	burst_ADP_results[resultsrow] = $integrated[480] - $integrated[80]		//Integral of aligned & subtracted wave, caluclated from 4ms to 24ms after spike peak
	burst_ADP_results_legend[resultsrow] = "Integral(mV*ms)_" + num2str(filenumber)
	resultsrow += 1
	filenumber +=1
		if(filenumber == removefile)
			filenumber +=1
		endif
while(filenumber <= endnumber)

//Display overlaid traces
counter = startnumber +1
display $"a"+num2str(startnumber)
do
	appendtograph $"a"+num2str(counter)
	counter +=1
		if(counter == removefile)
			counter +=1
		endif
while(counter <= endnumber)
ModifyGraph rgb=(0,0,0)
ModifyGraph height=800,width=2000

edit burst_ADP_results_legend,burst_ADP_results

end
