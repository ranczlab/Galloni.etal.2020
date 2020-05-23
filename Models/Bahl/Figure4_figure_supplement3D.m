clear

tuft = [560	555	555	555	555	555	555	555	555	550	550	550	550	550	550	550	550	550	550	545	545	545	545	545	545	545	545	545	545	545	545	545	540	540	540	540	540	540	540	540	540	540	540	540	540	540	540	540	540	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530];
tuft_trunk = [595	595	590	585	585	580	580	580	575	575	570	570	570	570	565	565	565	565	560	560	560	560	560	555	555	555	555	555	555	550	550	550	550	550	550	550	550	545	545	545	545	545	545	545	545	545	545	540	540	540	540	540	540	540	540	540	540	540	540	540	540	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	535	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530	530];
na = [NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	NaN	590	590	595	580	570	560	550	545	535	530];

i_h = 0:0.01:1;

hold on
plot(i_h,tuft,'k','linewidth',1)
mdl = fitlm(i_h,tuft);
x_regression = [0,1];
y_regression = mdl.Coefficients.Estimate(1) + mdl.Coefficients.Estimate(2) * x_regression;
%plot(x_regression,y_regression,'Color','b','Linestyle','--','LineWidth',1)
txt = strcat('tuft only, r2=',num2str(mdl.Rsquared.Ordinary),', p=',num2str(mdl.Coefficients.pValue(2)));
text(0.1,0.19,txt);

plot(i_h,tuft_trunk,'k','linewidth',2)
%([0,0.2])
mdl = fitlm(i_h,tuft_trunk);
x_regression = [0,1];
y_regression = mdl.Coefficients.Estimate(1) + mdl.Coefficients.Estimate(2) * x_regression;
%plot(x_regression,y_regression,'Color','g','Linestyle','--','LineWidth',1)
txt = strcat('tuft & trunk, r2=',num2str(mdl.Rsquared.Ordinary),', p=',num2str(mdl.Coefficients.pValue(2)));
text(0.1,0.175,txt);

plot(i_h,na,'--k')
%([0,0.2])
mdl = fitlm(i_h,na);
x_regression = [0,1];
y_regression = mdl.Coefficients.Estimate(1) + mdl.Coefficients.Estimate(2) * x_regression;
%plot(x_regression,y_regression,'Color','g','Linestyle','--','LineWidth',1)
txt = strcat('tuft & trunk, r2=',num2str(mdl.Rsquared.Ordinary),', p=',num2str(mdl.Coefficients.pValue(2)));
text(0.1,0.175,txt);

xlabel('gHCN(%)')
ylabel('critical length (um)')
ylim([500,600])
set(gca,'Fontsize',10)
set(gca,'TickDir','out');
box off
