load('Figure2_figure_supplement1.mat')

all = [V1_1p5;V1_2;V2_1p5;V2_2];

subplot(5,1,1)
    [h,u] = raincloud_plot('X',all,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0.7,0.7,0.7]);  
    xlim([0,250])
    set(gca,'TickDir','out') 
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('All data')
    
    all_mean = num2str(nanmean(all));
    all_std = num2str(nanstd(all));
    txt1 = strcat('mean=',all_mean,' +- ',all_std);
    text(150,0.008,txt1,'FontSize',15)
    
subplot(5,1,2)
    [h,u] = raincloud_plot('X',V1_1p5,'box_on',1,'box_dodge',1,'band_width',15,...
        'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[1,0.2,0.2]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V1 - 1.5mM CaCl2')
    
    V1_mean1p5 = num2str(mean(V1_1p5));
    V1_std1p5 = num2str(std(V1_1p5));
    txt1 = strcat('mean=',V1_mean1p5,' +- ',V1_std1p5);
    text(150,0.008,txt1,'FontSize',15)

subplot(5,1,3)
    [h,u] = raincloud_plot('X',V2_1p5,'box_on',1,'box_dodge',1,'band_width',15,...
        'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0,0.5,1]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V2m - 1.5mM CaCl2')
    
    V2_mean1p5 = num2str(mean(V2_1p5));
    V2_std1p5 = num2str(std(V2_1p5));
    txt1 = strcat('mean=',V2_mean1p5,' +- ',V2_std1p5);
    text(150,0.008,txt1,'FontSize',15)
    
subplot(5,1,4)
    [h,u] = raincloud_plot('X',V1_2,'box_on',1,'box_dodge',1,'band_width',15,...
        'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[1,0.2,0.2]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V1 - 2mM CaCl2')
    
    V1_mean2 = num2str(mean(V1_2));
    V1_std2 = num2str(std(V1_2));
    txt1 = strcat('mean=',V1_mean2,' +- ',V1_std2);
    text(150,0.008,txt1,'FontSize',15)
    
subplot(5,1,5)
    [h,u] = raincloud_plot('X',V2_2,'box_on',1,'box_dodge',1,'band_width',15,...
        'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0,0.5,1]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V2 - 2mM CaCl2')
    
    V2_mean2 = num2str(mean(V2_2));
    V2_std2 = num2str(std(V2_2));
    txt1 = strcat('mean=',V2_mean2,' +- ',V2_std2);
    text(150,0.008,txt1,'FontSize',15)
    
    
xlabel('Integral (ms*mV)','FontSize',40)
set(gcf, 'Position', [1000, 1000, 700, 1300])

%% Statistics

%Two-sample Kolmogorov-Smirnov test
[h,p,D] = kstest2(V1_1p5,V1_2);
txt3 = strcat('V1: Two-sample K-S test, p=',num2str(p),', D=',num2str(D));
text(120,-0.002,txt3,'FontSize',15)

[h,p,D] = kstest2(V2_1p5,V2_2);
txt4 = strcat('V2m: Two-sample K-S test, p=',num2str(p),', D=',num2str(D))
text(120,-0.005,txt4,'FontSize',15)

% %Wilcoxon rank sum test (aka Mann-Whitney U-test)
% [p,h] = ranksum(V1_1p5,V1_2);
% stats = num2str(p);
% txt3 = strcat('V1: Wilcoxon rank sum test, p=',stats);
% text(140,-0.002,txt3,'FontSize',15)
% 
% [p,h] = ranksum(V2_1p5,V2_2);
% stats = num2str(p);
% txt4 = strcat('V2: Wilcoxon rank sum test, p=',stats);
% text(140,-0.005,txt4,'FontSize',15)
