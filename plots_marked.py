import interface
import keys

#indicates wether to mark lockdown features in plot
MARKED = False

##selected keys category 1.a.
#overall break ins hotels
plot_breakin = interface.create_months_plot(keys.overallbreakins, keys.title_breakins, marked=True, marked2=True, m_label="Closed hotel industry", m2_label = "Opened hotel industry \n subject to conditions")
interface.save_plot(plot_breakin, keys.title_breakins, marked=True)
#shoplifting,robbery and theft on streets
plot_robbery = interface.create_months_plot(keys.robbery_and_theft_onstreets, keys.title_robbery, marked=True, mrange = [2,4.5, 10.5,11], marked2=True, m_label="Closed retail industry", m2_range=[4.5,10.5], m2_label="Opened retail industry \n subject to conditions")
interface.save_plot(plot_robbery, keys.title_robbery, marked=True)
#ecstasy
plot_ecstasy = interface.create_months_plot(keys.ecstasy, keys.title_ecs, marked=True, marked2=True, m_label="Closed bars and clubs", mrange=[2,4.5,9.5,11], m2_range=[4.5,9.5], m2_label="Closed indoor clubs \n cancelled festivals")
interface.save_plot(plot_ecstasy, keys.title_ecs, marked=True)

#-------------#

##selected keys category 1.b.
#sexual harassment and assault
plot_assault = interface.create_months_plot(keys.assault, keys.title_assault, mrange=[2,4.5,9.5,11], m_label="Contact restrictions")
interface.save_plot(plot_assault, keys.title_assault, marked=True)

#-------------#

##selected keys category 1.c.
#Child abuse
plot_abuse = interface.create_months_plot(keys.abuse, keys.title_abuse, mrange=[2,4, 10.5,11], m_label="Closed schools and \n kindergartens")
interface.save_plot(plot_abuse, keys.title_abuse, marked=True)
#selected drugs
plot_drugs = interface.create_months_plot(keys.drugs, keys.title_drugs, MARKED)
interface.save_plot(plot_drugs, keys.title_drugs, marked=True)

#--------------#

##selected keys category 2.
#violation of act against infection
plot_infection = interface.create_months_plot(keys.infection, keys.title_infection, marked3=False, mrange=[1.95,2.05], m_label="Start of pandemic \n in Germany")
interface.save_plot(plot_infection, keys.title_infection, marked=True)
#substity fraud
plot_subfraud = interface.create_months_plot(keys.subfraud, keys.title_subfraud, mrange=[2,4], marked3=False, m_label="Corona Soforthilfen")
interface.save_plot(plot_subfraud, keys.title_subfraud, marked=True)

#---------------#




