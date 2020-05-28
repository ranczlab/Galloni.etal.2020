data = csvread('Figure4_figure_supplement1c_inset.csv')';
baselines = csvread('Figure4_figure_supplement1c_inset_baselines.csv')';

x200 = [0:200/6:200]';
x300 = [0:300/6:300]';
x400 = [0:400/6:400]';
x500 = [0:500/6:500]';
x600 = [0:600/6:600]';

x_all = [x200,x300,x400,x500,x600];
lambda = [];
for i = 1:5 %for each length
    resting_potential =  mean(baselines(:,i));
    data(:,i) = data(:,i) - resting_potential;
    f = fit(x_all(:,i),data(:,i),'exp1');
    lambda(i) = -1/f.b;
end

hold on
trunk_length = [200,300,400,500,600];
scatter(trunk_length,lambda,500,'filled','k')

mdl = fitlm(trunk_length,lambda)
x_regression = [0,800];
y_regression = mdl.Coefficients.Estimate(1) + mdl.Coefficients.Estimate(2) * x_regression;
plot(x_regression,y_regression,'Color',[0.8 0.8 0.8],'Linestyle','--','LineWidth',1)

ylim([100,200])
xlim([0,800])
xlabel('trunk length (µm)')
ylabel('lambda (µm)')
set(gca,'Fontsize',30)
set(gca,'TickDir','out');
box off