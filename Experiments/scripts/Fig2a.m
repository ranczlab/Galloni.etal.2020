load('Fig2a.mat')

all = [V1;V2];

subplot(3,1,1)
    [h,u] = raincloud_plot('X',all,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0.7,0.7,0.7]);  
    xlim([0,250])
    set(gca,'TickDir','out') 
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('All data')
    
    all_mean = num2str(nanmean(all))
    all_std = num2str(nanstd(all))
    txt1 = strcat('mean=',all_mean,' +- ',all_std);
    text(150,0.008,txt1,'FontSize',20)
    
subplot(3,1,2)
    [h,u] = raincloud_plot('X',V2,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0,0.5,1]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V2m')
    
    V2_mean = num2str(nanmean(V2))
    V2_std = num2str(nanstd(V2))
    txt1 = strcat('mean=',V2_mean,' +- ',V2_std);
    text(150,0.008,txt1,'FontSize',20)

subplot(3,1,3)
    [h,u] = raincloud_plot('X',V1,'box_on',1,'box_dodge',1,'band_width',15,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[1,0.2,0.2]);  
    xlim([0,250])
    set(gca,'TickDir','out')
    set(gca,'FontSize',30)
    set(gca,'ytick',[])
    box off
    title('V1')
    
    V1_mean = num2str(nanmean(V1))
    V1_std = num2str(nanstd(V1))
    txt1 = strcat('mean=',V1_mean,' +- ',V1_std);
    text(150,0.008,txt1,'FontSize',20)
    
    
xlabel('Integral (ms*mV)','FontSize',40)
set(gcf, 'Position', [1000, 1000, 1000, 1000])

%% Statistics

%Kolmogorov-Smirnov test
[h,p,D] = kstest2(V1,V2)
txt2 = strcat('Two-sample K-S test, p=',num2str(p),', D=',num2str(D));
text(130,-0.004,txt2,'FontSize',20)

% %Wilcoxon rank sum test (aka Mann-Whitney U-test)
% [p,h] = ranksum(V1,V2)
% stats = num2str(p)
% txt2 = strcat('Wilcoxon rank sum test, p=',stats);
% text(130,-0.004,txt2,'FontSize',20)
