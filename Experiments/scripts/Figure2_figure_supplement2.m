load('Figure2_figure_supplement2.mat')

all = [V1_pooled;V2_pooled];

subplot(3,1,1)
    [h,u] = raincloud_plot('X',all,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0.7,0.7,0.7]);  
    xlim([0,250])
    set(gca,'TickDir','out') 
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('All data (V1 & V2m)')
    
    all_mean = num2str(nanmean(all));
    all_std = num2str(nanstd(all));
    txt1 = strcat('mean=',all_mean,' +- ',all_std);
    text(150,0.008,txt1,'FontSize',15)
    
subplot(3,1,2)
    [h,u] = raincloud_plot('X',V2_CTB,'box_on',1,'box_dodge',1,'band_width',15,...
        'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0,0.5,1]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V2m - CTB')
    
    CTB_mean = num2str(mean(V2_CTB));
    CTB_std = num2str(std(V2_CTB));
    txt1 = strcat('mean=',CTB_mean,' +- ',CTB_std);
    text(150,0.008,txt1,'FontSize',15)

subplot(3,1,3)
    [h,u] = raincloud_plot('X',V2_Glt,'box_on',1,'box_dodge',1,'band_width',15,...
        'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0,1,1]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V2m - Glt25d2')
    
    Glt_mean = num2str(mean(V2_Glt));
    Glt_std = num2str(std(V2_Glt));
    txt1 = strcat('mean=',Glt_mean,' +- ',Glt_std);
    text(150,0.015,txt1,'FontSize',15)

    
    
xlabel('Integral (ms*mV)','FontSize',40)
set(gcf, 'Position', [1000, 1000, 800, 1000])

%% Statistics

%Kolmogorov-Smirnov test
[h,p,D] = kstest2(V2_CTB,V2_Glt);
stats = num2str(p);
txt1 = strcat('V1: Kolmogorov-Smirnov test, p=',num2str(p),', D=',num2str(D));
text(120,0.005,txt1,'FontSize',15)


%Wilcoxon rank sum test (aka Mann-Whitney U-test)
% [p,h] = ranksum(V2_CTB,V2_Glt)
% stats = num2str(p);
% txt3 = strcat('V1: Wilcoxon rank sum test, p=',stats);
% text(140,-0.002,txt3,'FontSize',15)

