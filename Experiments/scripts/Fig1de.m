clear
load('Fig1de.mat')

x = [50,60,70,80,90,100,110,120,130,140,150,160,200];

subplot(1,3,1)
    scatter(x,V1_example,100,'k','filled')
    
    xlim([50,200])
    ylim([-50,200])
    xlabel('frequency (Hz)')
    ylabel('ADP integral (mV*ms)')
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    title('V1')

    ADP_max1 = num2str(max(V1_example))
    txt1 = strcat('max = ',ADP_max1);
    text(100,-40,txt1,'FontSize',20)
    title('V1')
    
subplot(1,3,2)
    scatter(x,V2_example,100,'k','filled')
    
    xlim([50,200])
    ylim([-50,200])
    xlabel('frequency (Hz)')
    ylabel('ADP integral (mV*ms)')
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    title('V2m')

    ADP_max2 = num2str(max(V2_example))
    txt1 = strcat('max = ',ADP_max2);
    text(100,-40,txt1,'FontSize',20)
    
    
subplot(1,3,3)

    hold on
    critFreq_all = [critFreq_V1;critFreq_V2];
    histogram(critFreq_all,[45:10:205],'FaceColor',[1 0.2 0.2])
    histogram(critFreq_V2,[45:10:205],'FaceColor',[0 0 1])

    V1_mean = num2str(mean(critFreq_V1));
    V1_std = num2str(std(critFreq_V1));
    V2_mean = num2str(mean(critFreq_V2));
    V2_std = num2str(std(critFreq_V2));
    all_mean = num2str(mean(critFreq_all));
    all_std = num2str(std(critFreq_all));

    [h,p] = ttest2(critFreq_V1,critFreq_V2)

    txt1 = strcat('V1 = ',V1_mean,' +-',V1_std);
    text(120,8,txt1,'FontSize',20)
    txt2 = strcat('V2 = ',V2_mean,' +-',V2_std);
    text(120,7,txt2,'FontSize',20)
    txt3 = strcat('all = ',all_mean,' +-',all_std);
    text(120,6,txt3,'FontSize',20)


    xlim([45,210])
    xlabel('critical freq. (Hz)')
    ylabel('no. of cells')
    box off
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)

set(gcf, 'Position', [500, 1000, 1500, 500])
