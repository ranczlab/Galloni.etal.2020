clear

Hay_long_symbol = '*r';
Hay_short_symbol = '*b';
Bahl_symbol = 's';
sz_l = 200;
sz_s = 200;
sz_b = 200;
sz = 100;
sz2 = 35;
alpha = 0.8;

%% Load data

load('Figure2_figure_supplement3.mat');
pooled_data = [dataV1;dataV2];
bursting = [V1_cfADP;V2_cfADP];
labels = {'V1','V2'};

%% define variables
RMP_V1 = dataV1(:,1);
RMP_V2 = dataV2(:,1);
RMP_Hay_long = data_models(1,1);
RMP_Hay_short = data_models(2,1);
RMP_Bahl200 = data_models(3,1);
RMP_Bahl300 = data_models(4,1);
RMP_Bahl400 = data_models(5,1);
RMP_Bahl500 = data_models(6,1);
RMP_Bahl600 = data_models(7,1);

Rn_V1 = dataV1(:,2);
Rn_V2 = dataV2(:,2);
Rn_Hay_long = data_models(1,2);
Rn_Hay_short = data_models(2,2);
Rn_Bahl200 = data_models(3,2);
Rn_Bahl300 = data_models(4,2);
Rn_Bahl400 = data_models(5,2);
Rn_Bahl500 = data_models(6,2);
Rn_Bahl600 = data_models(7,2);

rheobase_V1 = dataV1(:,3);
rheobase_V2 = dataV2(:,3);
rheobase_Hay_long = data_models(1,3);
rheobase_Hay_short = data_models(2,3);
rheobase_Bahl200 = data_models(3,3);
rheobase_Bahl300 = data_models(4,3);
rheobase_Bahl400 = data_models(5,3);
rheobase_Bahl500 = data_models(6,3);
rheobase_Bahl600 = data_models(7,3);

sag_amplitude_V1 = dataV1(:,4);
sag_amplitude_V2 = dataV2(:,4);
sag_amplitude_Hay_long = data_models(1,4);
sag_amplitude_Hay_short = data_models(2,4);
sag_amplitude_Bahl200 = data_models(3,4);
sag_amplitude_Bahl300 = data_models(4,4);
sag_amplitude_Bahl400 = data_models(5,4);
sag_amplitude_Bahl500 = data_models(6,4);
sag_amplitude_Bahl600 = data_models(7,4);

sag_steadystate_V1 = dataV1(:,5);
sag_steadystate_V2 = dataV2(:,5);

burst_ratio_V1 = dataV1(:,6:37);
burst_ratio_V2 = dataV2(:,6:37);
burst_ratio_Hay_long = max(data_models(1,6:37));
burst_ratio_Hay_short = max(data_models(2,6:37));
burst_ratio_Bahl200 = max(data_models(3,6:37));
burst_ratio_Bahl300 = max(data_models(4,6:37));
burst_ratio_Bahl400 = max(data_models(5,6:37));
burst_ratio_Bahl500 = max(data_models(6,6:37));
burst_ratio_Bahl600 = max(data_models(7,6:37));

burst_threshold_V1 = dataV1(:,38);
burst_threshold_V2 = dataV2(:,38);

burst_trace_analysed_V1 = dataV1(:,39);
burst_trace_analysed_V2 = dataV2(:,39);

burstISIs_V1 = dataV1(:,40:69);
burstISIs_V2 = dataV2(:,40:69);
burstISIs_Hay_long = data_models(1,40:69);
burstISIs_Hay_short = data_models(2,40:69);
burstISIs_Bahl200 = data_models(3,40:69);
burstISIs_Bahl300 = data_models(4,40:69);
burstISIs_Bahl400 = data_models(5,40:69);
burstISIs_Bahl500 = data_models(6,40:69);
burstISIs_Bahl600 = data_models(7,40:69);

burstAHPs_V1 = dataV1(:,70:99);
burstAHPs_V2 = dataV2(:,70:99);
burst_AHP_Hay_long = max(data_models(1,70:99));
burst_AHP_Hay_short = max(data_models(2,70:99));
burst_AHP_Bahl200 = max(data_models(3,70:99));
burst_AHP_Bahl300 = max(data_models(4,70:99));
burst_AHP_Bahl400 = max(data_models(5,70:99));
burst_AHP_Bahl500 = max(data_models(6,70:99));
burst_AHP_Bahl600 = max(data_models(7,70:99));

burst_spikes_V1 =  dataV1(:,100:130);
burst_spikes_V2 =  dataV2(:,100:130);
burst_spikes_Hay_long = data_models(1,100:130)-295;
burst_spikes_Hay_short = data_models(2,100:130)-295;
burst_spikes_Bahl200 = data_models(3,100:130)-295;
burst_spikes_Bahl300 = data_models(4,100:130)-295;
burst_spikes_Bahl400 = data_models(5,100:130)-295;
burst_spikes_Bahl500 = data_models(6,100:130)-295;
burst_spikes_Bahl600 = data_models(7,100:130)-295;

FI_steadystate_V1 = dataV1(:,131:163);
FI_steadystate_V2 = dataV2(:,131:163);

FI_burst_V1 = dataV1(:,164:196);
FI_burst_V2 = dataV2(:,164:196);

FI_all_V1 = dataV1(:,197:229);
FI_all_V2 = dataV2(:,197:229);

%% Generate plot


subplot_rows = 3;
subplot_cols = 3;
plot_number = 1;

subplot(subplot_rows,subplot_cols,plot_number) %RMP
    plot_dataV1 = RMP_V1;
    plot_dataV2 = RMP_V2;
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));

    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);

    x1 = ones(1,length(plot_dataV1));
    x2 = 2*ones(1,length(plot_dataV2));

    hold on
    scatter(x1,plot_dataV1,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_dataV2,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)   

    scatter(1.3,RMP_Hay_long,sz_l,Hay_long_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,RMP_Hay_short,sz_s,Hay_short_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,RMP_Bahl200,sz_b,[0.8 0.8 0.8],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.6,RMP_Bahl300,sz_b,[0.6 0.6 0.6],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.5,RMP_Bahl400,sz_b,[0.4 0.4 0.4],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.4,RMP_Bahl500,sz_b,[0.2 0.2 0.2],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.3,RMP_Bahl600,sz_b,[0 0 0],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)

    xlim([0,3])
    ylim([-80,-55])
    xticks([1,2])
    xticklabels(labels)
    ylabel('RMP (mV)')
    text(0.1,-57,txt,'Fontsize',15)

    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off
    
    plot_number = plot_number+1;

subplot(subplot_rows,subplot_cols,plot_number) %Rn
    plot_dataV1 = Rn_V1;
    plot_dataV2 = Rn_V2;
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));

    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);

    x1 = ones(1,length(plot_dataV1));
    x2 = 2*ones(1,length(plot_dataV2));

    hold on    
    scatter(x1,plot_dataV1,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_dataV2,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    scatter(1.3,Rn_Hay_long,sz_l,Hay_long_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,Rn_Hay_short,sz_s,Hay_short_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,Rn_Bahl200,sz_b,[0.8 0.8 0.8],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.6,Rn_Bahl300,sz_b,[0.6 0.6 0.6],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.5,Rn_Bahl400,sz_b,[0.4 0.4 0.4],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.4,Rn_Bahl500,sz_b,[0.2 0.2 0.2],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.3,Rn_Bahl600,sz_b,[0 0 0],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)

    xlim([0,3])
    ylim([0,150])
    xticks([1,2])
    xticklabels(labels)
    ylabel('input resistance (MOhm)')
    text(0.1,140,txt,'Fontsize',15);
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off

    plot_number = plot_number+1;

   
subplot(subplot_rows,subplot_cols,plot_number) %rheobase
    plot_dataV1 = rheobase_V1;
    plot_dataV2 = rheobase_V2;
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));

    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);

    hold on
    x1 = ones(length(plot_dataV1),1);
    x2 = 2*ones(length(plot_dataV2),1);

    scatter(x1,plot_dataV1,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_dataV2,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    scatter(1.3,rheobase_Hay_long,sz_l,Hay_long_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,rheobase_Hay_short,sz_s,Hay_short_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,rheobase_Bahl200,sz_b,[0.8 0.8 0.8],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.6,rheobase_Bahl300,sz_b,[0.6 0.6 0.6],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.5,rheobase_Bahl400,sz_b,[0.4 0.4 0.4],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.4,rheobase_Bahl500,sz_b,[0.2 0.2 0.2],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.3,rheobase_Bahl600,sz_b,[0 0 0],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)

    xlim([0,3])
    ylim([0,400])
    xticks([1,2])
    xticklabels(labels)
    ylabel('rheobase (pA)')
    text(0.1,280,txt,'Fontsize',15)    
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off

    plot_number = plot_number+1;

    
subplot(subplot_rows,subplot_cols,plot_number) %sag
    plot_dataV1 = sag_amplitude_V1;
    plot_dataV2 = sag_amplitude_V2;
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));
    
    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);

    x1 = ones(1,length(plot_dataV1));
    x2 = 2*ones(1,length(plot_dataV2));

    hold on
    scatter(x1,plot_dataV1,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_dataV2,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    scatter(1.3,sag_amplitude_Hay_long,sz_l,Hay_long_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,sag_amplitude_Hay_short,sz_s,Hay_short_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,sag_amplitude_Bahl200,sz_b,[0.8 0.8 0.8],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.6,sag_amplitude_Bahl300,sz_b,[0.6 0.6 0.6],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.5,sag_amplitude_Bahl400,sz_b,[0.4 0.4 0.4],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.4,sag_amplitude_Bahl500,sz_b,[0.2 0.2 0.2],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.3,sag_amplitude_Bahl600,sz_b,[0 0 0],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)

    xlim([0,3])
    ylim([0,6])
    xticks([1,2])
    xticklabels(labels)
    ylabel('sag amplitude (mV)')
    text(0.1,5.7,txt,'Fontsize',15)
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off
    plot_number = plot_number+1;
    
    
subplot(subplot_rows,subplot_cols,plot_number) %burst ratio V1/V2
    plot_dataV1 = max(burst_ratio_V1')';
    plot_dataV2 = max(burst_ratio_V2')';
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));
    
    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);
    
    x1 = ones(1,length(plot_dataV1));
    x2 = 2*ones(1,length(plot_dataV2));

    hold on
    scatter(x1,plot_dataV1,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_dataV2,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    scatter(1.3,burst_ratio_Hay_long,sz_l,Hay_long_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,burst_ratio_Hay_short,sz_s,Hay_short_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,burst_ratio_Bahl200,sz_b,[0.8 0.8 0.8],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.6,burst_ratio_Bahl300,sz_b,[0.6 0.6 0.6],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.5,burst_ratio_Bahl400,sz_b,[0.4 0.4 0.4],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.4,burst_ratio_Bahl500,sz_b,[0.2 0.2 0.2],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.3,burst_ratio_Bahl600,sz_b,[0 0 0],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)

    xlim([0,3])
    ylim([0,60])
    xticks([1,2])
    xticklabels(labels)
    ylabel('max burst ratio, ISI(n) / ISI(n-1)')
    text(0.1,58,txt,'Fontsize',15)
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off
    plot_number = plot_number+1;

    
subplot(subplot_rows,subplot_cols,plot_number) %burst AHP V1/V2
    plot_dataV1 = max(burstAHPs_V1')';
    plot_dataV2 = max(burstAHPs_V2')';
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));
    
    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);

    x1 = ones(1,length(plot_dataV1));
    x2 = 2*ones(1,length(plot_dataV2));

    hold on
    scatter(x1,plot_dataV1,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_dataV2,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    scatter(1.3,burst_AHP_Hay_long,sz_l,Hay_long_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,burst_AHP_Hay_short,sz_s,Hay_short_symbol,'MarkerFaceAlpha',alpha)
    scatter(1.7,burst_AHP_Bahl200,sz_b,[0.8 0.8 0.8],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.6,burst_AHP_Bahl300,sz_b,[0.6 0.6 0.6],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.5,burst_AHP_Bahl400,sz_b,[0.4 0.4 0.4],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.4,burst_AHP_Bahl500,sz_b,[0.2 0.2 0.2],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)
    scatter(1.3,burst_AHP_Bahl600,sz_b,[0 0 0],Bahl_symbol,'filled','MarkerFaceAlpha',alpha)

    xlim([0,3])
    ylim([0,50])
    xticks([1,2])
    xticklabels(labels)
    ylabel('max burst AHP (mV)')
    text(0.1,45,txt,'Fontsize',15)
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off
    plot_number = plot_number+1;


subplot(subplot_rows,subplot_cols,plot_number) %number of burst spikes

    %count spikes before the largest increase in ISI
    n_spikesV1 = [];
    n_spikesV2 = [];
    n_spikes_models = [];
    for cell = 1:size(burstISIs_V1,1)
        d = diff(burstISIs_V1(cell,:));
        [m,idx] = max(d);
        n_spikesV1(cell) = idx+1;
    end
    
    for cell = 1:size(burstISIs_V2,1)
        d = diff(burstISIs_V2(cell,:));
        [m,idx] = max(d);
        n_spikesV2(cell) = idx+1;
    end
    
    for cell = 1:size(data_models,1)
        d = diff(burstISIs_V2(cell,:));
        d = diff(data_models(cell,40:69));
        [m,idx] = max(d);
        n_spikes_models(cell) = idx+1;
    end    
    plot_dataV1 = n_spikesV1';
    plot_dataV2 = n_spikesV2';
    plot_data_models = n_spikes_models';
    
    [h,p] = ttest2(plot_dataV1,plot_dataV2);
    txt = strcat('t-test, p=',num2str(p));
    
    meanV1 = nanmean(plot_dataV1);
    SD_V1 = nanstd(plot_dataV1);
    meanV2 = nanmean(plot_dataV2);
    SD_V2 = nanstd(plot_dataV2);

    hold on
    binrange = 1:6;
    counts1 = histc(n_spikesV1,binrange);
    counts2 = histc(n_spikesV2,binrange);
    counts3 = counts1+counts2;
    
    bar(binrange,counts3,'FaceColor',[0.3 0.5 1],'BarWidth',1)
    bar(binrange,counts1,'FaceColor',[1 0.3 0.3],'BarWidth',1)

    xlim([0,6])
    ylim([0,50])
    xlabel('no. of burst spikes')
    ylabel('cells')
    text(1,50,txt,'Fontsize',15)
    box off
    set(gca,'TickDir','out')
    set(gca,'FontSize',15)
    plot_number = plot_number+1;

    
subplot(subplot_rows,subplot_cols,plot_number) %burst ratio cfADP/no cfADP
    data_ADP = pooled_data(bursting==1,:);
    data_noADP = pooled_data(bursting==0,:);
    labels = {'burst','no burst'};
    burst_ratio_ADP = data_ADP(:,6:37);
    burst_ratio_noADP = data_noADP(:,6:37);
    
    plot_data_ADP = max(burst_ratio_ADP')';
    plot_data_noADP = max(burst_ratio_noADP')';
    
    [h,p] = ttest2(plot_data_ADP,plot_data_noADP);
    txt = strcat('t-test, p=',num2str(p));
    
    meanV1 = nanmean(plot_data_ADP);
    SD_V1 = nanstd(plot_data_ADP);
    meanV2 = nanmean(plot_data_noADP);
    SD_V2 = nanstd(plot_data_noADP);

    x1 = ones(1,length(plot_data_ADP));
    x2 = 2*ones(1,length(plot_data_noADP));

    hold on
    scatter(x1,plot_data_ADP,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_data_noADP,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,60])
    xticks([1,2])
    xticklabels(labels)
    ylabel('max burst ratio, ISI(n) / ISI(n-1)')
    text(0.1,58,txt,'Fontsize',15)
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off
    plot_number = plot_number+1;
    
subplot(subplot_rows,subplot_cols,plot_number) %burst AHP ADP/no ADP
    data_ADP = pooled_data(bursting==1,:);
    data_noADP = pooled_data(bursting==0,:);
    labels = {'burst','no burst'};
    burstAHPs_ADP = data_ADP(:,6:37);
    burstAHPs_noADP = data_noADP(:,6:37);
    
    plot_data_ADP = max(burstAHPs_ADP')';
    plot_data_noADP = max(burstAHPs_noADP')';
    
    [h,p] = ttest2(plot_data_ADP,plot_data_noADP);
    txt = strcat('t-test, p=',num2str(p));
    
    meanV1 = nanmean(plot_data_ADP);
    SD_V1 = nanstd(plot_data_ADP);
    meanV2 = nanmean(plot_data_noADP);
    SD_V2 = nanstd(plot_data_noADP);

    x1 = ones(1,length(plot_data_ADP));
    x2 = 2*ones(1,length(plot_data_noADP));

    hold on
    scatter(x1,plot_data_ADP,sz,'r','MarkerFaceAlpha',alpha)
    errorbar(0.8,meanV1,SD_V1,'.','MarkerSize',sz2,'color','k','linewidth',2)
    scatter(x2,plot_data_noADP,sz,'b','MarkerFaceAlpha',alpha)
    errorbar(2.2,meanV2,SD_V2,'.','MarkerSize',sz2,'color','k','linewidth',2)

    xlim([0,3])
    ylim([0,50])
    xticks([1,2])
    xticklabels(labels)
    ylabel('max burst AHP (mV)')
    text(0.1,50,txt,'Fontsize',15)
    set(gca,'Fontsize',15)
    set(gca,'TickDir','out');
    box off
    
set(gcf, 'Position', [800, 1000, 1400, 800])












