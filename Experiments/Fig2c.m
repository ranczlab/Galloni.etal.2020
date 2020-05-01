load('Fig2c.mat')

% Scatter plot
subplot(4,2,1:4)
grouping = [ones(1,length(morphologiesV1)),2*ones(1,length(morphologiesV2))];
x = [morphologiesV1',morphologiesV2'];
y = [ADPs_V1',ADPs_V2'];
s = scatterhist(x,y,'Group',grouping,'Kernel','on','Bandwidth',[35,35;16,16],...
   'Location','SouthWest','MarkerSize',9,'Marker','ooo','Color','rbc');

%Linear model
hold on
mdl = fitlm(x,y)
x_regression = [0,550];
y_regression = mdl.Coefficients.Estimate(1) + mdl.Coefficients.Estimate(2) * x_regression;
plot(x_regression,y_regression,'Color','k','Linestyle','--','LineWidth',2)

%Graph properties
ylabel('Integral dV (mV*ms)','FontSize',20)
xlabel('Apical trunk length (µm)','FontSize',20)
set(gca,'tickdir','out')
box off
legend('V1','V2','Linear regression')
set(gcf, 'Position', [700, 1000, 550, 500])

% Print text
slope = num2str(mdl.Coefficients.Estimate(2));
intercept = num2str(mdl.Coefficients.Estimate(1));
pval = num2str(mdl.Coefficients.pValue(2));

txt1 = strcat('p =',pval);
txt2 = strcat('y =',slope,'x ',intercept);
text(180,160,txt1)
text(180,180,txt2)

V1_mean = num2str(nanmean(morphologiesV1));
V1_std = num2str(nanstd(morphologiesV1));
txt3 = strcat('V1 mean=',V1_mean,' +- ',V1_std);
text(400,-155,txt3)

V2_mean = num2str(nanmean(morphologiesV2));
V2_std = num2str(nanstd(morphologiesV2));
txt4 = strcat('V2 mean=',V2_mean,' +- ',V2_std);
text(100,-155,txt4)

[h,p] = ttest2(morphologiesV1,morphologiesV2);
txt5 = strcat('two-sample t-test, p =',num2str(p));
text(250,-140,txt5)
