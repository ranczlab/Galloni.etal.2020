import argparse

parser = argparse.ArgumentParser()
parser.add_argument('tuft_gca_multiplier', metavar = 'gCA', type=str)
parser.add_argument('lowxy', metavar = 'lowxy', type=str)
parser.add_argument('hotspot_size', metavar = 'Hx', type=str)
parser.add_argument('LVA_volume', metavar = 'LVA')
args = parser.parse_args()

filetext = """
// Author: Etay Hay, 2011
//    Models of Neocortical Layer 5b Pyramidal Cells Capturing a Wide Range of
//    Dendritic and Perisomatic Active Properties
//    (Hay et al., PLoS Computational Biology, 2011) 
//
// Model of L5 Pyramidal Cell, constrained both for BAC firing and Current Step Firing


begintemplate L5PCbiophys
public biophys

proc biophys() {
	forsec $o1.all {
	  insert pas
		cm = 1
		Ra = 100
		e_pas = -90
	}

  forsec $o1.somatic {
	  insert Ca_LVAst 
	  insert Ca_HVA 
	  insert SKv3_1 
	  insert SK_E2 
	  insert K_Tst 
	  insert K_Pst 
	  insert Nap_Et2 
	  insert NaTa_t
		insert CaDynamics_E2
		insert Ih
		ek = -85
		ena = 50
		gIhbar_Ih = 0.0002
    g_pas = 0.0000338 
  	decay_CaDynamics_E2 = 460.0 
  	gamma_CaDynamics_E2 = 0.000501 
  	gCa_LVAstbar_Ca_LVAst = 0.00343 
  	gCa_HVAbar_Ca_HVA = 0.000992 
  	gSKv3_1bar_SKv3_1 = 0.693 
  	gSK_E2bar_SK_E2 = 0.0441 
  	gK_Tstbar_K_Tst = 0.0812 
  	gK_Pstbar_K_Pst = 0.00223 
  	gNap_Et2bar_Nap_Et2 = 0.00172 
  	gNaTa_tbar_NaTa_t = 2.04 
  }

	forsec $o1.apical {
		cm = 2
		insert Ih
  	insert SK_E2 
  	insert Ca_LVAst 
  	insert Ca_HVA 
  	insert SKv3_1 
  	insert NaTa_t 
  	insert Im 
  	insert CaDynamics_E2
		ek = -85
		ena = 50
    decay_CaDynamics_E2 = 122 
    gamma_CaDynamics_E2 = 0.000509 
    gSK_E2bar_SK_E2 = 0.0012 
  	gSKv3_1bar_SKv3_1 = 0.000261 
  	gNaTa_tbar_NaTa_t = 0.0213 
  	gImbar_Im = 0.0000675 
  	g_pas = 0.0000589 
	}
	$o1.distribute_channels("apic","gIhbar_Ih",2,-0.8696,3.6161,0.0,2.0870,0.00020000000) 
	   
   multiplier = %s
   lowxy = %s
   highxy = lowxy + %s
   LVA_volume = %s
   HVA_volume = 0.11 - LVA_volume
   
 $o1.distribute_channels("apic","gCa_LVAstbar_Ca_LVAst",3,1.000000,LVA_volume,lowxy,highxy, multiplier*0.0187000000) 
	$o1.distribute_channels("apic","gCa_HVAbar_Ca_HVA",3,1.000000,HVA_volume,lowxy,highxy, multiplier*0.0005550000) 
	

  forsec $o1.basal {
		cm = 2
		insert Ih
		gIhbar_Ih = 0.0002
  	g_pas = 0.0000467 
	}

  forsec $o1.axonal {
  	g_pas = 0.0000325 
	}
}

endtemplate L5PCbiophys
""" % (str(args.tuft_gca_multiplier), str(args.lowxy), str(args.hotspot_size), str(args.LVA_volume))

with open('models/L5PCbiophys3.hoc', 'w') as f:
    f.write(filetext)
    