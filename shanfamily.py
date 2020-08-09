#Import libraries
import pandas as pd

#Ignore warnings
import warnings
warnings.filterwarnings("ignore")

class ShanFamily:
  def __init__(self):
    self.df_family=family_initialize() 
    

#Get relations of a person based on the relationship
  def GET_RELATIONSHIP(self,Name,Relation):
    df_family=self.df_family
    if (Name.strip(' ')!=''):
      if Relation == 'Mother-In-Law':
        return (mother_in_law(Name,df_family))
      elif Relation == 'Father-In-Law':
        return (father_in_law(Name,df_family))
      elif Relation == 'Sister-In-Law':
        return (sis_in_law(Name,df_family))
      elif Relation == 'Brother-In-Law':
        return (bro_in_law(Name,df_family))
      elif Relation == 'Daughter':
        return (daughter(Name,df_family))
      elif Relation == 'Son':    
        return (son(Name,df_family))
      elif Relation == 'Mother':
        return (mother(Name,df_family))
      elif Relation == 'Father':
        return (father(Name,df_family))
      elif Relation == 'Sister':
        return (sister(Name,df_family))
      elif Relation == 'Brother':
        return (brother(Name,df_family))
      elif Relation == 'Paternal-Aunt':
        return (pat_aunt(Name,df_family))
      elif Relation == 'Paternal-Uncle':
        return(pat_uncle(Name,df_family))
      elif Relation == 'Maternal-Aunt':
        return(mat_aunt(Name,df_family))
      elif Relation == 'Maternal-Uncle':
        return(mat_uncle(Name,df_family))
      elif Relation == 'Siblings':
        return(siblings(Name,df_family))        
      elif Relation == 'Spouse':
          return (spouse(Name,df_family))
      return ('RELATION_NOT_VALID')
    return ('NAME_NOT_VALID')
    
  
  def ADD_CHILD(self,Mother,Name,Gender):
    df_family=self.df_family
    if (Gender == 'Female'):
      gender = 'F'
    elif (Gender  ==  'Male'):
      gender = 'M'
    else:
      return ('CHILD_ADDITION_FAILED_GENDER_NOT_VALID')
    #Check if child name already exists in family
    if (len(df_family[(df_family['name']==Name)])==0 and len(df_family[(df_family['spouse']==Name)])==0):
      #Check if mother exists
      if (check_if_name_exists(Mother,df_family)):
        #Check if mother in family_name and gender  is not female return
        if (Mother in df_family['name']):
          if (df_family[df_family['name'==Mother]]['gender']!='F'):
            return ('CHILD_ADDITION_FAILED_MOTHER_NOT_FEMALE')
        #Check if mother is in family_spouse and gender is not female return
        elif (Mother in df_family['spouse']):
          if (df_family[df_family['spouse'==Mother]]['gender']!='F'):
            return ('CHILD_ADDITION_FAILED_MOTHER_NOT_FEMALE')
        #Check if Name is not blank, find spouse and update the row for with spouse and reset other details for df_family and df_family 
        elif (Name.strip(' ')!=''):
          sp=spouse(Mother,df_family)
          if (sp != 'SPOUSE_NOT_FOUND'):        
            row = pd.DataFrame({'name':[Name],'mother':[Mother],'gender':[gender],'spouse':''} )
            self.df_family=df_family.append(row,ignore_index=True)
            self.df_family=family_update(self.df_family)
            return ('CHILD_ADDITION_SUCCEEDED')
          return ('CHILD_ADDITION_FAILED_MOTHER_NOT_MARRIED')
        return ('CHILD_ADDITION_FAILED_CHILDNAME_NOT_VALID')
      return ('CHILD_ADDITION_FAILED_MOTHER_NOT_FOUND')
    return ('CHILD_ADDITION_FAILED_CHILDNAME_EXISTS_IN_FAMILY')


        
  def ADD_SPOUSE(self,Name,Spouse) :
    df_family=self.df_family
    #Check if Spouse is not blank and check if name does not exist in family 
    if (Spouse.strip(' ')!='' and (check_if_name_exists('Spouse',df_family)==False) ):
      #Check if Name is present in family_name and name is not married and Name is not blank
      if ( Name.strip(' ')!=''):
        if (Name in list(df_family['name']) ):
          if ((df_family[df_family['name']==Name]['married']=='N').bool())  :
            row=df_family[df_family['name']==Name]
            row['spouse']=Spouse
            self.df_family.update(row)
            self.df_family=family_update(self.df_family)
            return ('SPOUSE_ADDITION_SUCCEEDED')
          return 'SPOUSE_ADDITION_FAILED_PERSON_ALREADY_MARRIED'
        return 'SPOUSE_ADDITION_FAILED_PERSON_NOT_IN_FAMILY'
      return 'SPOUSE_ADDITION_FAILED_PERSONNAME_NOT_VALID'
    return 'SPOUSE_ADDITION_FALIED_SPOUSENAME_NOT_VALID'

#To intialize on object creation
def family_initialize():
#Creating a dictonary to initialize the dataframe
    Family={
      'name':['Shan','Chit','Ish','Vich','Aras','Satya','Dritha','Tritha','Vritha','Vila','Chika','Jnki','Ahit','Asva','Vyas','Atya','Yodhan','Laki','Lavnya','Vasa','Kriya','Krithi']
      ,'gender':['M','M','M','M','M','F','F','F','M','F','F','F','M','M','M','F','M','M','F','M','M','F']    
      ,'mother':['','Anga','Anga','Anga','Anga','Anga','Amba','Amba','Amba','Lika','Lika','Chitra','Chitra','Satya','Satya','Satya','Dritha','Jnki','Jnki','Satvy','Krpi','Krpi']
      ,'spouse':['Anga','Amba','','Lika','Chitra','Vyan','Jaya','','','','','Arit','','Satvy','Krpi','','','','','','',''] 
      
    }
    #Initializing family dataframe
    df_fam=pd.DataFrame(Family)
    df_fam=family_update(df_fam)
    return df_fam

#Update other columns of df_family based on initialization
def family_update(df_fam):
    #Adding gender for spouse in family df
    df_fam['gender_spouse']=df_fam.apply(lambda x:x['spouse'] if x['spouse'] == '' else ('F' if (x['gender']  ==  'M') else 'M'),axis=1)
    #Adding info for Married
    df_fam['married']=df_fam.apply(lambda x:'N' if x['spouse'] == '' else 'Y',axis=1)
    #Adding number of children
    df_fam['cnt_of_children']=df_fam.apply(lambda x:len(df_fam[df_fam['mother']  ==  x['name']]) if (x['gender']  ==  'F' and x['married']  ==  'Y') else (len(df_fam[df_fam['mother']  ==  x['spouse']]) if (x['gender']  ==  'M' and x['married']  ==  'Y')  else 0),axis=1)
    #Adding number of siblings
    df_fam['cnt_of_siblings']=df_fam.apply(lambda x:len(df_fam[df_fam['mother']  ==  x['mother']])-1 if(len(df_fam[df_fam['mother']  ==  x['mother']])>1) else 0,axis=1)
    #Adding father from known data
    df_fam['father']=df_fam.apply(lambda x:''.join(df_fam[df_fam['spouse'] == x['mother']]['name']) if (x['mother'] in list(df_fam['spouse']) and len(x['mother'])>0) else (''.join(df_fam[df_fam['name'] == x['mother']]['spouse']) if (x['mother'] in list(df_fam['name'])) else ''),axis=1)
    #Adding siblings 
    df_fam['siblings']=df_fam.apply(lambda x:[y for y in list(df_fam[df_fam['mother'] == x['mother']]['name']) if y!=x['name']] if (len(df_fam[df_fam['mother'] == x['mother']])>1) else '' ,axis=1)
    #Adding son
    df_fam['son']=df_fam.apply(lambda x:list(df_fam[(df_fam['mother'] == x['name'])&(df_fam['gender'] == 'M')]['name'])   if (x['gender'] == 'F' and len(df_fam[(df_fam['mother'] == x['name'])&(df_fam['gender'] == 'M')])>0) else (list(df_fam[(df_fam['father'] == x['name'])&(df_fam['gender'] == 'M')]['name']) if (x['gender'] == 'M' and len(df_fam[(df_fam['father'] == x['name'])&(df_fam['gender'] == 'M')])>0) else '') ,axis=1)
    #Adding daughter
    df_fam['daughter']=df_fam.apply(lambda x:list(df_fam[(df_fam['mother'] == x['name'])&(df_fam['gender'] == 'F')]['name'])   if (x['gender'] == 'F' and len(df_fam[(df_fam['mother'] == x['name'])&(df_fam['gender'] == 'F')])>0) else (list(df_fam[(df_fam['father'] == x['name'])&(df_fam['gender'] == 'F')]['name']) if (x['gender'] == 'M' and len(df_fam[(df_fam['father'] == x['name'])&(df_fam['gender'] == 'F')])>0) else '') ,axis=1)
    #Adding brother
    df_fam['brother']=df_fam.apply(lambda x:[y for y in list(df_fam[(df_fam['gender'] == 'M')&(df_fam['mother'] == x['mother'])]['name'])  if y!=x['name']] if (len(df_fam[(df_fam['gender'] == 'M')&(df_fam['mother'] == x['mother'])])>1 and x['gender'] == 'M')   else (list(df_fam[(df_fam['gender'] == 'M')&(df_fam['mother'] == x['mother'])]['name']) if (len(df_fam[(df_fam['gender'] == 'M')&(df_fam['mother'] == x['mother'])])>0 and x['gender'] == 'F') else ''),axis=1)
    #Adding sister
    df_fam['sister']=df_fam.apply(lambda x:[y for y in list(df_fam[(df_fam['gender'] == 'F')&(df_fam['mother'] == x['mother'])]['name'])  if y!=x['name']] if (len(df_fam[(df_fam['gender'] == 'F')&(df_fam['mother'] == x['mother'])])>1 and x['gender'] == 'F')   else (list(df_fam[(df_fam['gender'] == 'F')&(df_fam['mother'] == x['mother'])]['name']) if (len(df_fam[(df_fam['gender'] == 'F')&(df_fam['mother'] == x['mother'])])>0 and x['gender'] == 'M') else ''),axis=1)
    
    return df_fam


#To check if name exists in family or not
def check_if_name_exists(Name,df_family):
  if (Name in list(pd.concat([df_family['name'],df_family['spouse']]).replace(to_replace='',value=np.nan).dropna())):
    return True
  else:
    return False

#To retrive the mother of a person
def mother(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name not in list(df_family['spouse']) ):
      mom=df_family.set_index('name',drop=True).loc[Name,'mother']
      # print(mom!='')
      if (str(mom)!=''):
        return mom
    
    return 'MOTHER_NOT_FOUND'
  return 'PERSON_NOT_FOUND'

#To retrive the father of a person
def father(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!='' ):
    if (Name not in list(df_family['spouse'])):
      dad=df_family.set_index('name',drop=True).loc[Name,'father']
      if (dad!=''):
        return dad
    return 'FATHER_NOT_FOUND'
      
  return 'PERSON_NOT_FOUND'

#To retrive the siblings of a person
def siblings(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name not in list(df_family['spouse']) ):
      sib=df_family.set_index('name',drop=True).loc[Name,'siblings']
      if (sib!=''):
        return ' '.join(sib)
    return 'SIBLINGS_NOT_FOUND'
      
  return 'PERSON_NOT_FOUND'

#To retrive the brother of a person
def brother(Name,df_family):
  if (check_if_name_exists(Name,df_family) ):
    if (Name not in list(df_family['spouse']) and Name!=''):
      bro=df_family.set_index('name',drop=True).loc[Name,'brother']
      if (bro!=''):
        return ' '.join(bro)
    return 'BROTHER_NOT_FOUND'
      
  return 'PERSON_NOT_FOUND'

#To retrive the sister of a person
def sister(Name,df_family):
  if (check_if_name_exists(Name,df_family) ):
    if (Name not in list(df_family['spouse']) and Name!=''):
      bro=df_family.set_index('name',drop=True).loc[Name,'sister']
      if (bro!=''):
        return ' '.join(bro)
    return 'SISTER_NOT_FOUND'
      
  return 'PERSON_NOT_FOUND'

#To retrive the son of a person
def son(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['spouse'])):
      son=df_family.set_index('spouse',drop=True).loc[Name,'son']
      if (son!=''):
        return ' '.join(son)
    elif (Name in list(df_family['name'])):
      son=df_family.set_index('name',drop=True).loc[Name,'son']
      if (son!=''):
        return ' '.join(son)
    return 'SON_NOT_FOUND'
      
  return 'PERSON_NOT_FOUND'

#To retrive the daughter of a person
def daughter(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['spouse'])):
      daug=df_family.set_index('spouse',drop=True).loc[Name,'daughter']
      
    elif (Name in list(df_family['name'])):
      daug=df_family.set_index('name',drop=True).loc[Name,'daughter']
    if (daug!=''):
      return ' '.join(daug)
    return 'DAUGHTER_NOT_FOUND'
      
  return 'PERSON_NOT_FOUND'

#To retrive the maternal uncle of a person
def mat_uncle(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['name'])):
      mom=mother(Name,df_family)
      if (mother!='MOTHER_NOT_FOUND'):
        bro=brother(mom,df_family)
        if (bro!='BROTHER_NOT_FOUND'):
          return bro  
    return 'MATERNAL_UNCLE_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

#To retrive the maternal aunt of a person
def mat_aunt(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['name'])):
      mom=mother(Name,df_family)
      if (mother!='MOTHER_NOT_FOUND'):
        sis=sister(mom,df_family)
        if (sis!='SISTER_NOT_FOUND'):
          return sis 
    return 'MATERNAL_AUNT_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

#To retrive the paternal uncle of a person
def pat_uncle(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['name'])):
      dad=father(Name,df_family)
      if (father!='FATHER_NOT_FOUND'):
        bro=brother(dad,df_family)
        if (bro!='BROTHER_NOT_FOUND'):
          return bro  
    return 'PATERNAL_UNCLE_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

#To retrive the paternal aunt of a person
def pat_aunt(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['name'])):
      dad=father(Name,df_family)
      if (father!='FATHER_NOT_FOUND'):
        sis=sister(dad,df_family)
        if (sis!='SISTER_NOT_FOUND'):
          return sis 
    return 'PATERNAL_AUNT_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

#To retrive the spouse of a person
def spouse(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''): 
    if (Name in list(df_family['spouse'])):
      sp=df_family.set_index('spouse',drop=True).loc[Name,'name']
    elif (Name in list(df_family['name'])):
      sp=df_family.set_index('name',drop=True).loc[Name,'spouse']
    if (sp!=''):
      return sp    
    return ('SPOUSE_NOT_FOUND')
  return ('PERSON_NOT_FOUND')

#To retrive the brother in law  of a person
def bro_in_law(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['spouse'])):
      sp=spouse(Name,df_family)
      if (spouse!='SPOUSE_NOT_FOUND'):
        bro_in_law=brother(sp,df_family)
        if (bro_in_law!='BROTHER_NOT_FOUND'):
          return bro_in_law
    return 'BROTHER_IN_LAW_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

#To retrive the sister in law of a person
def sis_in_law(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['spouse'])):
      sp=spouse(Name,df_family)
      if (spouse!='SPOUSE_NOT_FOUND'):
        sis_in_law=sister(sp,df_family)
        if (sis_in_law!='SISTER_NOT_FOUND'):
          return sis_in_law
    return 'SISTER_IN_LAW_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'


#To retrive the father in law of a person
def father_in_law(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['spouse'])):
      sp=spouse(Name,df_family)
      if (spouse!='SPOUSE_NOT_FOUND'):
        dad_in_law=father(sp,df_family)
        if (dad_in_law!='FATHER_NOT_FOUND'):
          return dad_in_law
    return 'FATHER_IN_LAW_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

#To retrive the mother in law of a person
def mother_in_law(Name,df_family):
  if (check_if_name_exists(Name,df_family)  and Name!=''):
    if (Name in list(df_family['spouse'])):
      sp=spouse(Name,df_family)
      if (spouse!='SPOUSE_NOT_FOUND'):
        mom_in_law=mother(sp,df_family)
        if (mom_in_law!='MOTHER_NOT_FOUND'):
          return mom_in_law
    return 'MOTHER_IN_LAW_NOT_FOUND'    
  return 'PERSON_NOT_FOUND'

