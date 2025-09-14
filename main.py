import lxml.etree as xet

document = xet.parse(file_path)


 # Hand desinfektion allgemeinstation
        
        #Hand_desinf_verbr_As = find_safe(document, "//Weitere_Informationen_Hygiene/Haendedesinfektion/Haendedesinfektionsmittelverbrauch_Allgemeinstationen_wurde_erhoben/Haendedesinfektionsmittelverbrauch_Allgemeinstationen", info)
        #Hand_desinf_verbr_As = find_safe(document, "//Haendedesinfektionsmittelverbrauch_Allgemeinstationen", info)
        Hand_desinf_verbr_As = tree.xpath("//Haendedesinfektionsmittelverbrauch_Allgemeinstationen")
        if Hand_desinf_verbr_As != []: HAND_AS= Hand_desinf_verbr_As[0].text
        
        if Hand_desinf_verbr_As == []:
            Hand_desinf_verbr_As = tree.xpath("//Haendedesinfektionsmittelverbrauch_Allgemeinstationen_Gesamtbericht/Haendedesinfektionsmittelverbrauch_Untere_Grenze")
            if Hand_desinf_verbr_As != []:
               # print ("In dem Krankenhaus: ", name, "wird so viel verbraucht: " ,Hand_desinf_verbr_As[0].text)
                HAND_AS = Hand_desinf_verbr_As[0].text
        if Hand_desinf_verbr_As == []:
            Hand_desinf_verbr_As = tree.xpath("//Haendedesinfektionsmittelverbrauch_Allgemeinstationen_wurde_nicht_erhoben")
            if Hand_desinf_verbr_As != []: Hand_desinf_verbr_As = ["wurde nicht erhoben"]
           # print("In dem Krankenhaus: ", name, " wurde nicht erhoben")
            HAND_AS = "nicht erhoben"

        if Hand_desinf_verbr_As == []:
            Hand_desinf_verbr_As = tree.xpath("//Haendedesinfektionsmittelverbrauch_wurde_nicht_erhoben")
            if Hand_desinf_verbr_As != []: Hand_desinf_verbr_As = ["wurde nicht erhoben"]
            #print("In dem Krankenhaus: ", name, " wurde nicht erhoben")
            HAND_AS = "nicht erhoben"
        if Hand_desinf_verbr_As == []: 
           # print("In dem Krankenhaus:", name, "ist man schmutzig")
            HAND_AS = "keine Angabe"
       # print("HAND: ", HAND_AS)
        
       
        Hand_desinf_verbr_Is = tree.xpath("//Haendedesinfektionsmittelverbrauch_Intensivstationen")
        if Hand_desinf_verbr_Is != []: HAND_IS= Hand_desinf_verbr_Is[0].text

        
        if Hand_desinf_verbr_Is == []:
            Hand_desinf_verbr_Is = tree.xpath("//Haendedesinfektionsmittelverbrauch_Intensivstationen_Gesamtbericht/Haendedesinfektionsmittelverbrauch_Untere_Grenze")
            if Hand_desinf_verbr_Is != []:
                #print ("In dem Krankenhaus: ", name, "wird so viel verbraucht: " ,Hand_desinf_verbr_Is[0].text)
                HAND_IS = Hand_desinf_verbr_Is[0].text
        if Hand_desinf_verbr_Is == []:
            Hand_desinf_verbr_Is = tree.xpath("//Haendedesinfektionsmittelverbrauch_Intensivstationen_wurde_nicht_erhoben")
            if Hand_desinf_verbr_Is != []: Hand_desinf_verbr_Is = ["wurde nicht erhoben"]
            #print("In dem Krankenhaus: ", name, " wurde nicht erhoben")
            HAND_IS = "nicht erhoben"

        if Hand_desinf_verbr_Is == []:
            Hand_desinf_verbr_Is = tree.xpath("//Haendedesinfektionsmittelverbrauch_wurde_nicht_erhoben")
            if Hand_desinf_verbr_Is != []: Hand_desinf_verbr_Is = ["wurde nicht erhoben"]
            #print("In dem Krankenhaus: ", name, " wurde nicht erhoben")
            HAND_IS = "nicht erhoben"
        if Hand_desinf_verbr_Is == []: 
            #print("In dem Krankenhaus:", name, "ist man schmutzig")
            HAND_IS = "keine Angabe"
       # print("Hand_is: ", HAND_IS)
        
        
       
        Fortbildungspflichtige = tree.xpath("//Fortbildungspflichtige")  #//Qualitaetssicherung
        Nachweispflichtige = tree.xpath("//Nachweispflichtige")
        Fortbildungsnachweis_erbracht_habende = tree.xpath("//Fortbildungsnachweis_Erbracht_Habende")#[0].text
        
        if Fortbildungspflichtige !=[]:
            #print(Fortbildungspflichtige[0].text)
            Fort_pfl = Fortbildungspflichtige[0].text
        else: Fort_pfl = "keine Angabe"
            
        if Nachweispflichtige !=[]:
            #print(Nachweispflichtige[0].text)
            Nachw_pfl = Nachweispflichtige[0].text
        else: Nachw_pfl = "keine Angabe"
        
        if Fortbildungsnachweis_erbracht_habende !=[]:
           # print(Fortbildungsnachweis_erbracht_habende[0].text)
            Fort_erb_hab = Fortbildungsnachweis_erbracht_habende[0].text
        else: Fort_erb_hab = "keine Angabe"
