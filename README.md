# LICENSE_RETRIVER_API
Retrieve the details of given license no

## Achievements:

    1) Solving Captcha is not needed.
    
    2) More faster retrieval of data as there is no need of captcha solving.
    
## To run the program
    
    1) Install requirements.txt
    
    2) Enter git clone https://github.com/sudhan247/LICENSE_RETRIVER_API.git
    
    3) Enter cd LICENSE_RETRIVER_API
    
    4) Enter python scrapper.py
    
    5) Then enter the License No and DOB in specified format
    
    
## SampleData
    
    License No: DL-0420110149646
    
    DOB: 09-02-1976

## Format

    Driving Licence number can be entered in any of the following formats: DL-1420110012345 or DL14 20110012345
    Total number of input characters should be exactly 16 (including space or '-').
    If you hold an old driving license with a different format, please convert the format as per below rule before entering.
    SS-RRYYYYNNNNNNN OR SSRR YYYYNNNNNNN
    Where
    SS - Two character State Code (like RJ for Rajasthan, TN for Tamil Nadu etc)
    RR - Two digit RTO Code
    YYYY - 4-digit Year of Issue (For Example: If year is mentioned in 2 digits, say 99, then it should be converted to 1999. Similarly use 2012 for 12).
    Rest of the numbers are to be given in 7 digits. If there are less number of digits, then additional 0's(zeros) may be added to make the total 7.
    For example: If the Driving Licence Number is RJ-13/DLC/12/ 123456 then please enter RJ-1320120123456 OR RJ13 20120123456.
