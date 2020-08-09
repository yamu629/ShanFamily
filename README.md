# ShanFamily
Assumptions for family:
- Every family member has unique name
- Every individual has only 1 spouse 
- Every individual has only 1 mother 
- Every individual has only 1 father
- Of an individual and spouse, either is from outside family and the other is born within family
- No other outisde family member family details will be added except as spouse
- Child can be added only for a person with spouse
- Spouse is always of opposite gender
- Spouse can only be added for an existing family member who is unmarried
- Mother is always of Female gender

 There are 3 methods available for the user
* GET_RELATIONSHIP "Name" "Relation"
* ADD_CHILD "Mother" "Child" "Gender", Gender in full form with first letter in CAPS
* ADD_SPOUSE "Person" "Spouse"

Assumptions for above methods:
- For GET_RELATIONSHIP
  * Method for relation should exist
  * Person should exist as spouse or born in family
  * Valid inputs as relation is 'Daughter','Son','Father','Mother','Brother', 'Sister' , 'Father-In-Law','Mother-In-Law','Brother-In-Law', 'Sister-In-Law' , 
  'Maternal-Aunt', 'Maternal-Uncle','Paternal-Aunt','Paternal-Uncle','Siblings'
  
- For ADD_CHILD
  * Mother should exist in family then only Child gets added
  * Mother should be married then only child gets added
  * Mother should be female then only child gets added
  * Child's Name cannot exist for any family member already 
	
- For ADD_SPOUSE, 
  * Person should exist not as spouse but as original member born in family
  * Spouse Name cannot exist for any family member already
  * Person should not be already married

Error case response:
- GET_RELATIONSHIP
  * returns RELATION_NOT_VALID if method for relation does not exist.
  * returns NAME_NOT_VALID if blanks or spaces is given as Person
  
- ADD_CHILD
  * If Gender Invalid, returns CHILD_ADDITION_FAILED_GENDER_NOT_VALID
  * If Mother is not female, returns CHILD_ADDITION_FAILED_MOTHER_NOT_FEMALE
  * If Mother is not married, returns CHILD_ADDITION_FAILED_MOTHER_NOT_MARRIED
  * If Childname is blank or spaces, returns CHILD_ADDITION_FAILED_CHILDNAME_NOT_VALID
  * If Mother is not found in familt, returns CHILD_ADDITION_FAILED_MOTHER_NOT_FOUND
  * If Childname exists in family, returns CHILD_ADDITION_FAILED_CHILDNAME_EXISTS_IN_FAMILY
  
- ADD_SPOUSE
  * returns SPOUSE_ADDITION_FAILED_PERSON_ALREADY_MARRIED, if Person is already married
  * returns SPOUSE_ADDITION_FAILED_PERSON_NOT_IN_FAMILY, if Person is not born in family
  * returns SPOUSE_ADDITION_FAILED_PERSONNAME_NOT_VALID, if Person Name is blank or spaces
  * returns SPOUSE_ADDITION_FALIED_SPOUSENAME_NOT_VALID, if Spouse Name is blank or spaces or is in family
