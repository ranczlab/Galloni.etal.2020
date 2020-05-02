clear
load('Figure2_figure_supplement4.mat');

subplot_rows = 4;
subplot_cols = 5;
plot_number = 1;

subplot(subplot_rows,subplot_cols,plot_number) %Basal dendrite length
    basal_length_V1 = dataV1(:,3);
    meanV1 = mean(basal_length_V1);
    SD_V1 = std(basal_length_V1);

    basal_length_V2 = dataV2(:,3);
    meanV2 = mean(basal_length_V2);
    SD_V2 = std(basal_length_V2);

    x1 = ones(1,length(basal_length_V1));
    x2 = 2*ones(1,length(basal_length_V2));

    hold on
    scatter(x1,basal_length_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,basal_length_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,5000])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('total basal dendrite length (µm)')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(basal_length_V1,basal_length_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,600,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %Tuft dendrite length (total)
    tuft_length_V1 = dataV1(:,5);
    meanV1 = mean(tuft_length_V1);
    SD_V1 = std(tuft_length_V1);

    tuft_length_V2 = dataV2(:,5);
    meanV2 = mean(tuft_length_V2);
    SD_V2 = std(tuft_length_V2);

    x1 = ones(1,length(tuft_length_V1));
    x2 = 2*ones(1,length(tuft_length_V2));

    hold on
    scatter(x1,tuft_length_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)
    scatter(x2,tuft_length_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,5000])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('total tuft dendrite length (µm)')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(tuft_length_V1,tuft_length_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,1000,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %total dendrite length
    apical_length_V1 = dataV1(:,2);
    meanV1 = mean(apical_length_V1);
    SD_V1 = std(apical_length_V1);

    apical_length_V2 = dataV2(:,2);
    meanV2 = mean(apical_length_V2);
    SD_V2 = std(apical_length_V2);

    x1 = ones(1,length(apical_length_V1));
    x2 = 2*ones(1,length(apical_length_V2));

    hold on
    scatter(x1,apical_length_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,apical_length_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,10000])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('total dendrite length (µm)')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(apical_length_V1,apical_length_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,1000,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %trunk length
    trunk_length_V1 = dataV1(:,25);
    meanV1 = mean(trunk_length_V1);
    SD_V1 = std(trunk_length_V1);
    
    trunk_length_V2 = dataV2(:,25);
    meanV2 = mean(trunk_length_V2);
    SD_V2 = std(trunk_length_V2);

    x1 = ones(1,length(trunk_length_V1));
    x2 = 2*ones(1,length(trunk_length_V2));

    hold on
    scatter(x1,trunk_length_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,trunk_length_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,600])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('trunk length (µm)')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(trunk_length_V1,trunk_length_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,50,txt,'Fontsize',15)
    plot_number = plot_number+1;
     
subplot(subplot_rows,subplot_cols,plot_number) %Basal branch points
    basal_nodes_V1 = dataV1(:,11);
    meanV1 = mean(basal_nodes_V1);
    SD_V1 = std(basal_nodes_V1);

    basal_nodes_V2 = dataV2(:,11);
    meanV2 = mean(basal_nodes_V2);
    SD_V2 = std(basal_nodes_V2);

    x1 = ones(1,length(basal_nodes_V1));
    x2 = 2*ones(1,length(basal_nodes_V2));

    hold on
    scatter(x1,basal_nodes_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,basal_nodes_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,50])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('basal branch points')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(basal_nodes_V1,basal_nodes_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,5,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %Tuft branch points
    tuft_nodes_V1 = dataV1(:,10);
    meanV1 = mean(tuft_nodes_V1);
    SD_V1 = std(tuft_nodes_V1);
    
    tuft_nodes_V2 = dataV2(:,10);
    meanV2 = mean(tuft_nodes_V2);
    SD_V2 = std(tuft_nodes_V2);

    x1 = ones(1,length(tuft_nodes_V1));
    x2 = 2*ones(1,length(tuft_nodes_V2));

    hold on
    scatter(x1,tuft_nodes_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,tuft_nodes_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,50])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('tuft branch points')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(tuft_nodes_V1,tuft_nodes_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,5,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %Total branch points
    total_nodes_V1 = dataV1(:,13);
    meanV1 = mean(total_nodes_V1);
    SD_V1 = std(total_nodes_V1);

    total_nodes_V2 = dataV2(:,13);
    meanV2 = mean(total_nodes_V2);
    SD_V2 = std(total_nodes_V2);

    x1 = ones(1,length(total_nodes_V1));
    x2 = 2*ones(1,length(total_nodes_V2));

    hold on
    scatter(x1,total_nodes_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,total_nodes_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([40,120])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('total branch points')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(total_nodes_V1,total_nodes_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,50,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %Oblique dendrites
    primary_obliques_V1 = dataV1(:,14);
    meanV1 = mean(primary_obliques_V1);
    SD_V1 = std(primary_obliques_V1);

    primary_obliques_V2 = dataV2(:,14);
    meanV2 = mean(primary_obliques_V2);
    SD_V2 = std(primary_obliques_V2);

    x1 = ones(1,length(primary_obliques_V1));
    x2 = 2*ones(1,length(primary_obliques_V2));

    hold on
    scatter(x1,primary_obliques_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,primary_obliques_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,25])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('no. of primary obliques')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(primary_obliques_V1,primary_obliques_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,5,txt,'Fontsize',15)
    plot_number = plot_number+1;

    
subplot(subplot_rows,subplot_cols,plot_number) %convex hull 2D area
    area_V1 = dataV1(:,22);
    meanV1 = mean(area_V1);
    SD_V1 = std(area_V1);

    area_V2 = dataV2(:,22);
    meanV2 = mean(area_V2);
    SD_V2 = std(area_V2);
    
    x1 = ones(1,length(area_V1));
    x2 = 2*ones(1,length(area_V2));

    hold on
    scatter(x1,area_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,area_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,400000])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('2D convex hull area (µm2)')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(area_V1,area_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,50000,txt,'Fontsize',15)
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %largest sholl radius
    largest_sholl_V1 = dataV1(:,24);
    meanV1 = mean(largest_sholl_V1);
    SD_V1 = std(largest_sholl_V1);

    largest_sholl_V2 = dataV2(:,24);
    meanV2 = mean(largest_sholl_V2);
    SD_V2 = std(largest_sholl_V2);

    x1 = ones(1,length(largest_sholl_V1));
    x2 = 2*ones(1,length(largest_sholl_V2));

    hold on
    scatter(x1,largest_sholl_V1,'r','filled','MarkerFaceAlpha',0.8)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',25,'color','k','linewidth',2)

    scatter(x2,largest_sholl_V2,'b','filled','MarkerFaceAlpha',0.8)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',25,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,1000])
    xticks([1,2])
    xticklabels({'V1','V2'})
    ylabel('largest sholl radius (µm)')
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
	box off

    [h,p] = ttest2(largest_sholl_V1,largest_sholl_V2);
    txt = strcat('t-test, p=',num2str(p));
    text(0.1,100,txt,'Fontsize',15)
    plot_number = plot_number+1;

%% Bregma plots

subplot(subplot_rows,subplot_cols,plot_number)
    [h,u] = raincloud_plot('X',bregmaV1,'box_on',1,'box_dodge',1,'band_width',0.3,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[1,0.2,0.2]);  
    xlim([-6,-1])
    set(gca,'TickDir','out')
    set(gca,'YTick',[])
    box off
    xlabel('Distance from bregma (mm)','FontSize',15)
    
    [h,p] = ttest2(bregmaV1,bregmaV2);
    txt = strcat('t-test, p=',num2str(p));
    text(100,0,txt,'Fontsize',15)
    plot_number = plot_number+1;

subplot(subplot_rows,subplot_cols,plot_number+4)
    [h,u] = raincloud_plot('X',bregmaV2,'box_on',1,'box_dodge',1,'band_width',0.3,'bxfacecl',[1,1,1],'cloud_edge_col', [0.8 0.8 0.8],'point_size',50,'color',[0.5,0.5,1]);  
    xlim([-6,-1])
    set(gca,'TickDir','out')
    set(gca,'YTick',[])
    box off
    xlabel('Distance from bregma (mm)','FontSize',15)
    
    [h,p] = ttest2(bregmaV1,bregmaV2);
    txt = strcat('t-test, p=',num2str(p));
    text(-5.5,0.8,txt,'Fontsize',15)
    
%%
%Sholl plots
subplot(subplot_rows,subplot_cols,plot_number:plot_number+1)
    sholl_radius = 10:10:820;
    sholl_data_V1 = dataV1(:,26:end);
    sholl_data_V2 = dataV2(:,26:end);
    
    sholl_meanV1 = nanmean(sholl_data_V1);
    std_V1 = nanstd(sholl_data_V1);
    sholl_meanV2 = nanmean(sholl_data_V2);
    std_V2 = nanstd(sholl_data_V2);

    hold on
    shadedErrorBar(sholl_radius,sholl_meanV1,std_V1,'lineprops','r');
    shadedErrorBar(sholl_radius,sholl_meanV2,std_V2,'lineprops','b');


    xlim([0,700])
    ylim([0,50])
    set(gca,'TickDir','out');
    box off
    xlabel('Distance (µm)')
    ylabel('Intersections')
    title('V1 Sholl plot')
    set(gca,'FontSize',13)
    set(gca,'linewidth',1)


   
set(gcf, 'Position', [800, 1000, 1400, 1000])





