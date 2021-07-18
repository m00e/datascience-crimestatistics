import interface
import keys

#indicates wether to mark lockdown features in plot
MARKED = False

## all criminal offences ##
plot_allg = interface.create_months_plot(keys.allg, keys.title_allg, MARKED, marked3=MARKED)
interface.save_plot(plot_allg, keys.title_allg)

## selected keys category 1.a ##
#overall break ins hotels
plot_breakin = interface.create_months_plot(keys.overallbreakins, keys.title_breakins, MARKED, marked3=MARKED)
interface.save_plot(plot_breakin, keys.title_breakins)
#shoplifting,robbery and theft on streets
plot_robbery = interface.create_months_plot(keys.robbery_and_theft_onstreets, keys.title_robbery, MARKED, marked3=MARKED)
interface.save_plot(plot_robbery, keys.title_robbery)
#ecstasy
plot_ecstasy = interface.create_months_plot(keys.ecstasy, keys.title_ecs, MARKED, marked3=MARKED)
interface.save_plot(plot_ecstasy, keys.title_ecs)

## selected keys category 1.b ##
#sexual harassment and assault
plot_assault = interface.create_months_plot(keys.assault, keys.title_assault, MARKED, marked3=MARKED)
interface.save_plot(plot_assault, keys.title_assault)

## selected keys category 1.c ##
#Child abuse
plot_abuse = interface.create_months_plot(keys.abuse, keys.title_abuse, MARKED, marked3=MARKED)
interface.save_plot(plot_abuse, keys.title_abuse)
#selected drugs
plot_drugs = interface.create_months_plot(keys.drugs, keys.title_drugs, MARKED, marked3=MARKED)
interface.save_plot(plot_drugs, keys.title_drugs)

## selected keys category 2 ##
#violation of act against infection
plot_infection = interface.create_months_plot(keys.infection, keys.title_infection, MARKED, marked3=MARKED)
interface.save_plot(plot_infection, keys.title_infection)
#substity fraud
plot_subfraud = interface.create_months_plot(keys.subfraud, keys.title_subfraud, MARKED, marked3=MARKED)
interface.save_plot(plot_subfraud, keys.title_subfraud)

## selected keys category 3 ##
#cybercrime
plot_cybercrime = interface.create_months_plot(keys.cybercrime, keys.title_cybercrime, marked=MARKED, marked3=MARKED)
interface.save_plot(plot_cybercrime, keys.title_cybercrime)
#fraud
plot_fraud = interface.create_months_plot(keys.fraud, keys.title_fraud, marked=MARKED, marked3=MARKED)
interface.save_plot(plot_fraud, keys.title_fraud)
