clear

V1_BAC = 10;
V1_noBAC = 11;
V1_total_BAC = V1_BAC + V1_noBAC;
V1_BAC_percentage = 100 * V1_BAC / V1_total_BAC;

V1_ADP = 26;
V1_noADP = 15;
V1_total_ADP = V1_ADP + V1_noADP;
V1_ADP_percentage = 100 * V1_ADP / V1_total_ADP;


V2_BAC = 1;
V2_noBAC = 17;
V2_total_BAC = V2_BAC + V2_noBAC;
V2_BAC_percentage = 100 * V2_BAC / V2_total_BAC;

V2_ADP = 9;
V2_noADP = 40;
V2_total_ADP = V2_ADP + V2_noADP;
V2_ADP_percentage = 100 * V2_ADP / V2_total_ADP;


BAC_percentages = [V1_BAC_percentage,V2_BAC_percentage];
ADP_percentages = [V1_ADP_percentage,V2_ADP_percentage];

b = bar([BAC_percentages;ADP_percentages],'FaceColor','flat');
b(1).CData = [1 0.4 0.4];
b(2).CData = [0.4 0.5 1];
ylim([0,100])

xticklabels({'BAC','ADP'})
ylabel('% supralinear neurons')
set(gca,'Fontsize',20)
set(gca,'TickDir','out');
box off

txt1 = strcat(num2str(V1_BAC),'/',num2str(V1_total_BAC));
text(0.71,54,txt1,'FontSize',25)
txt2 = strcat(num2str(V2_BAC),'/',num2str(V2_total_BAC));
text(1.02,12,txt2,'FontSize',25)
txt3 = strcat(num2str(V1_ADP),'/',num2str(V1_total_ADP));
text(1.71,70,txt3,'FontSize',25)
txt4 = strcat(num2str(V2_ADP),'/',num2str(V2_total_ADP));
text(2.04,25,txt4,'FontSize',25)

txt5 = "Fisher's exact test:";
text(0.6,90,txt5,'FontSize',20)

fisher_BAC = [V1_BAC,V2_BAC;V1_noBAC,V2_noBAC];
[h,p,stats] = fishertest(fisher_BAC);
txt6 = strcat("p=",num2str(p));
text(0.7,65,txt6,'FontSize',20)

fisher_ADP = [V1_ADP,V2_ADP;V1_noADP,V2_noADP];
[h,p,stats] = fishertest(fisher_ADP);
txt7 = strcat("p=",num2str(p));
text(1.7,81,txt7,'FontSize',20)


