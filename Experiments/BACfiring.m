clear
data1 = csvread("L1_stim_data_V1.csv",2,8);
data2 = csvread("L1_stim_data_V2.csv",2,8);

time = data1(1,4:end);
dt = time(2)-time(1);
low_stim = data1(2:3:62,4:end);
med_stim = data1(3:3:63,4:end);
high_stim = data1(4:3:64,4:end);
bursting = data1(2:3:62,1);
n_cells = size(low_stim,1);

range1 = 200/dt:250/dt; %Time window containing L1 stim
range2 = 600/dt:650/dt; %Time window containing somatic spike
range3 = 400/dt:450/dt; %Time window containing coincident stimulation

%% V1
% Low stim
subplot(2,2,1)
coincidence_vector = [];
sum_vector = [];
hold on
for cell = 1:n_cells
    
    raw_trace = low_stim(cell,:);

    %Measure integrals of L1 stim, spike, and coincidence stim
    baseline = mean(raw_trace(150:200/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    L1stim = trapz(time(range1),raw_trace(range1));
    
    baseline = mean(raw_trace(550:600/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    spike = trapz(time(range2),raw_trace(range2));
    
    baseline = mean(raw_trace(350:400/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    coincidence = trapz(time(range3),raw_trace(range3));
    linear_sum = L1stim + spike;
    
    %Store data
    coincidence_vector(cell) = coincidence;
    sum_vector(cell) = linear_sum;
end

plot([1,3],[sum_vector',coincidence_vector'],'linewidth',2,'color','k')
means = [mean(sum_vector),mean(coincidence_vector)];
errors = [std(sum_vector),std(coincidence_vector)]./sqrt(n_cells);
errorbar([0.5,3.5],means,errors,'o','color','k','linewidth',3)

xlim([0,4])
ylim([0,1400])
xticks([1,3])
xticklabels({'linear sum','coincident stim'})
ylabel('Integral (mV*ms)')
set(gca,'Fontsize',15)
title('V1 Low stim (~5mV EPSP)')

[h,p] = ttest(coincidence_vector,sum_vector);
txt = strcat('paired t-test, p=',num2str(p));
text(1.2,100,txt,'Fontsize',15)
    

% Medium stim
subplot(2,2,2)
coincidence_vector_burst = [];
sum_vector_burst = [];
coincidence_vector_noburst = [];
sum_vector_noburst = [];
hold on
for cell = 1:n_cells
    
    %Measure and subtract baseline
    raw_trace = med_stim(cell,:);

    %Measure integrals of L1 stim, spike, and coincidence stim
    baseline = mean(raw_trace(150:200/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    L1stim = trapz(time(range1),raw_trace(range1));
    
    baseline = mean(raw_trace(550:600/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    spike = trapz(time(range2),raw_trace(range2));
    
    baseline = mean(raw_trace(350:400/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    coincidence = trapz(time(range3),raw_trace(range3));
    linear_sum = L1stim + spike;
    
    if bursting(cell) == 1
        col = 'r';
        coincidence_vector_burst = [coincidence_vector_burst,coincidence];
        sum_vector_burst = [sum_vector_burst,linear_sum];
    else
        col = 'k';
        coincidence_vector_noburst = [coincidence_vector_noburst,coincidence];
        sum_vector_noburst = [sum_vector_noburst,linear_sum];
    end
    plot([1,3],[linear_sum,coincidence],'linewidth',2,'color',col)

    

end

means_burst = [mean(sum_vector_burst),mean(coincidence_vector_burst)];
errors_burst = [std(sum_vector_burst),std(coincidence_vector_burst)]./sqrt(sum(bursting));
errorbar([0.5,3.5],means_burst,errors_burst,'o','color','r','linewidth',3)

means_noburst = [mean(sum_vector_noburst),mean(coincidence_vector_noburst)];
errors_noburst = [std(sum_vector_noburst),std(coincidence_vector_noburst)]./sqrt(n_cells-sum(bursting));
errorbar([0.5,3.5],means_noburst,errors_noburst,'o','color','k','linewidth',3)

xlim([0,4])
ylim([0,1400])
xticks([1,3])
xticklabels({'linear sum','coincident stim'})
set(gca,'Fontsize',15)
title('V1 Medium stim (~spike threshold)')

[h,p] = ttest(coincidence_vector_burst,sum_vector_burst);
txt = strcat('paired t-test, p=',num2str(p));
text(1.2,100,txt,'Fontsize',15,'Color','r')

[h,p] = ttest(coincidence_vector_noburst,sum_vector_noburst);
txt = strcat('paired t-test, p=',num2str(p));
text(1.2,200,txt,'Fontsize',15)


%% V2

time = data2(1,4:end);
dt = time(2)-time(1);
low_stim = data2(2:3:53,4:end);
med_stim = data2(3:3:54,4:end);
high_stim = data2(4:3:55,4:end);
bursting = data2(2:3:55,1);
n_cells = size(low_stim,1);


%Low stim
subplot(2,2,3)
coincidence_vector = [];
sum_vector = [];
hold on
for cell = 1:n_cells
    raw_trace = low_stim(cell,:);

    %Measure integrals of L1 stim, spike, and coincidence stim
    baseline = mean(raw_trace(150:200/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    L1stim = trapz(time(range1),raw_trace(range1));
    
    baseline = mean(raw_trace(550:600/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    spike = trapz(time(range2),raw_trace(range2));
    
    baseline = mean(raw_trace(350:400/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    coincidence = trapz(time(range3),raw_trace(range3));
    linear_sum = L1stim + spike;
    
    %Store data
    coincidence_vector(cell) = coincidence;
    sum_vector(cell) = linear_sum;
end

plot([1,3],[sum_vector',coincidence_vector'],'linewidth',2,'color','k')
means = [mean(sum_vector),mean(coincidence_vector)];
errors = [std(sum_vector),std(coincidence_vector)]./sqrt(n_cells);
errorbar([0.5,3.5],means,errors,'o','color','k','linewidth',3)

xlim([0,4])
ylim([0,1400])
xticks([1,3])
xticklabels({'linear sum','coincident stim'})
ylabel('Integral (mV*ms)')
set(gca,'Fontsize',15)
title('V2 Low stim (~5mV EPSP)')

[h,p] = ttest(coincidence_vector,sum_vector);
txt = strcat('paired t-test, p=',num2str(p));
text(1.2,100,txt,'Fontsize',15)

% Medium stim
subplot(2,2,4)
coincidence_vector2 = [];
sum_vector2 = [];
hold on
for cell = 1:n_cells    
    raw_trace = med_stim(cell,:);

    %Measure integrals of L1 stim, spike, and coincidence stim
    baseline = mean(raw_trace(150:200/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    L1stim = trapz(time(range1),raw_trace(range1));
    
    baseline = mean(raw_trace(550:600/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    spike = trapz(time(range2),raw_trace(range2));
    
    baseline = mean(raw_trace(350:400/dt)); %Measure and subtract baseline
    raw_trace = raw_trace - baseline;
    coincidence = trapz(time(range3),raw_trace(range3));
    linear_sum = L1stim + spike;
    
    if bursting(cell) == 1
        col = 'r';
    else
        col = 'k';
    end
    plot([1,3],[linear_sum,coincidence],'linewidth',2,'color',col)
    
    %Store data
    coincidence_vector2(cell) = coincidence;
    sum_vector2(cell) = linear_sum;
end

%plot([1,3],[coincidence_vector2,sum_vector2],'linewidth',2,'color','k')
means = [mean(sum_vector2),mean(coincidence_vector2)];
errors = [std(sum_vector2),std(coincidence_vector2)]./sqrt(n_cells);
errorbar([0.5,3.5],means,errors,'o','color','k','linewidth',3)

xlim([0,4])
ylim([0,1400])
xticks([1,3])
xticklabels({'linear sum','coincident stim'})
set(gca,'Fontsize',15)
title('V2 Medium stim (~spike threshold)')
box off
set(gca,'TickDir','out')


[h,p] = ttest(coincidence_vector2,sum_vector2);
txt = strcat('paired t-test, p=',num2str(p));
text(1.2,100,txt,'Fontsize',15)



set(gcf, 'Position', [500, 1000, 1000, 800])

