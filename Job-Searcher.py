try:import re,urllib3;from colorama import Fore;from requests import get,post,packages;from time import sleep
except ModuleNotFoundError:exit('[!] Download The Missing Module !')
try:packages.urllib3.disable_warnings()
except:urllib3.disable_warnings()


class Job:


    def __init__(self,email):
        self.email=email    


    def Single_Job_Searcher(self):
        Keyword=input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] Job Title or Keywords : ')
        pageSize=2;page=1
        head={'Host': 'careers.stc.com.sa','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json; charset=utf-8','Content-Length': '240','Origin': 'https://careers.stc.com.sa','Referer': 'https://careers.stc.com.sa/?source=TweakPY-Telegram','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'}
        try:
            rq0=post('https://careers.stc.com.sa/routers/job-alert/1.0/ej/private/job/alert',headers=head,json={"data":{"request":{"userId":f"{email}","searchKey":[],"selectedFilters":{"categories":[],"jobTypes":[{"value":"Experienced","key":"EXPERIENCED"},{"value":"Fresh Graduate","key":"FRESHER"},{"value":"Trainee","key":"TRAINEE"}]},"hiringType":"external"}}},allow_redirects=True,verify=False)
            rq1=post('https://careers.stc.com.sa/routers/jobs-search/1.0/ej/en/public/jobs/search',headers=head,json={"data":{"request":{"userId":"","searchKey":[f"{Keyword}"],"selectedFilters":{"categories":[],"jobTypes":[]},"hiringType":"external","pageNum":f"{page}","pageSize":f"{pageSize}"}}},allow_redirects=True,verify=False)
        except:pass;exit('[!] Fetal Error sorry ...')
       
        if 'Error contact admin please' in rq0.text:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Failed to save your email {email}');print('\n')
        elif 'success' in rq0.text:print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] We will inform You if anything new came out in your email {email}');print('\n')
        else:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Failed to save your email {email}');print('\n')
        
        if '{"data":{"jobs":[]}}' in rq1.text:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] 0 Jobs Found ..');exit('[+] We will inform You if anything new came out ...')
        elif 'paginationDetails' in rq1.text:
            try:print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}]',rq1.json()['data']["paginationDetails"]["totalRecords"],'Jobs Found !');print('\n')
            except:pass 

            try:
                Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[0]
                Job_Title=re.findall('"jobTitle":"(.*?)"',rq1.text)[0]
                Job_company=re.findall('"company":"(.*?)"',rq1.text)[0]
                try:Job_jobDescription=re.findall('"jobDescription":"(.*?)"',rq1.text)[0]
                except:Job_jobDescription='Null'
                Job_jobPostingDate=re.findall('"jobPostingDate":"(.*?)"',rq1.text)[0]
                try:Job_jobType=re.findall('"jobType":"(.*?)"',rq1.text)[0]
                except:Job_jobType='Null'
                Job_jobLevel=re.findall('"jobLevel":"(.*?)"',rq1.text)[0]
                Job_category=re.findall('"category":"(.*?)"',rq1.text)[0]
                Job_yearsOfExperience=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[0]
                Job_organization=re.findall('"organization":"(.*?)"',rq1.text)[0]
                try:Job_lastModificationDate=re.findall('"lastModificationDate":"(.*?)"',rq1.text)[0]
                except:Job_lastModificationDate='Null'
                Job_locationEn=re.findall('"locationEn":"(.*?)"',rq1.text)[0]

                #print section 
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job ID :',Job_id)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Title :',Job_Title)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Company :',Job_company)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Description :',Job_jobDescription)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Posting Date :',Job_jobPostingDate)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Type :',Job_jobType)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Level :',Job_jobLevel)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Category :',Job_category)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Years of Experience :',Job_yearsOfExperience)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Org :',Job_organization)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Last Modification Date :',Job_lastModificationDate)
                print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Location :',Job_locationEn)
            except:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Sorry ..');exit()
            ifinterested=int(input(f'\n\n[{Fore.LIGHTRED_EX}?{Fore.RESET}] Are You interested in This Job :\n\n[{Fore.LIGHTRED_EX}1{Fore.RESET}] Yes, I would like to get the job details\n[{Fore.LIGHTRED_EX}2{Fore.RESET}] Nah, I want to get another job\n\n[{Fore.LIGHTRED_EX}#{Fore.RESET}] Your choose : '))
            if ifinterested==1:
                rq2=get(f'https://careers.stc.com.sa/routers/jobs/1.0/ej/en/public/jobs/{Job_id}?user_id=undefined',headers={'Host': 'careers.stc.com.sa','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},allow_redirects=True,verify=False)
                if 'There was an error, Please try again later' in rq2.text:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Try Later ..');exit()
                else:
                    try:
                        Job_d=rq2.json()['data']['jobDetails']
                        JobPurpose=Job_d['jobPurposeEn']
                        keyResponsibilities=Job_d['keyResponsibilitiesEn']
                        qualification=Job_d['qualification']
                        major=Job_d['major']
                        natureOfExperience=Job_d['natureOfExperience']
                        englishLevel=Job_d['englishLevel']
                        try:certification=Job_d['certification']
                        except:certification='Null'
                        JobCategory=Job_d['jobCategory']
                        generalManagement=Job_d['generalManagement']
                        department=Job_d['department']
                        section=Job_d['section']
                        sector=Job_d['sector']
                        
                        #print section 
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Purpose :',JobPurpose)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Title :',keyResponsibilities)
                        print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Job Qualifications :\n\n')
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Degree :',qualification)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Major :',major)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Nature Of Experience :',natureOfExperience)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job English Level :',englishLevel)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Certification :',certification)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Category :',JobCategory)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job General Management :',generalManagement)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Department :',department)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Section :',section)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Sector :',sector)
                        print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job url : https://careers.stc.com.sa/?source=TweakPY-Telegram/jobs/jobResults#/jobs/jobDescription/{Job_id}')
                    except:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Sorry ..');exit()
            else:    
                try:
                    Job_id=re.findall(',{"jobId":"(.*?)"',rq1.text)[0]
                    Job_Title=re.findall(',"jobTitle":"(.*?)",',rq1.text)[1]
                    Job_company=re.findall('"company":"(.*?)"',rq1.text)[1]
                    try:Job_jobDescription=re.findall('"jobDescription":"(.*?)"',rq1.text)[1]
                    except:Job_jobDescription='Null'
                    Job_jobPostingDate=re.findall('"jobPostingDate":"(.*?)"',rq1.text)[1]
                    try:Job_jobType=re.findall('"jobType":"(.*?)"',rq1.text)[1]
                    except:Job_jobType='Null'
                    Job_jobLevel=re.findall('"jobLevel":"(.*?)"',rq1.text)[1]
                    Job_category=re.findall('"category":"(.*?)"',rq1.text)[1]
                    Job_yearsOfExperience=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[1]
                    Job_organization=re.findall('"organization":"(.*?)"',rq1.text)[1]
                    try:Job_lastModificationDate=re.findall('"lastModificationDate":"(.*?)"',rq1.text)[1]
                    except:Job_lastModificationDate='Null'
                    Job_locationEn=re.findall('"locationEn":"(.*?)"',rq1.text)[1]
                    
                    #print section 
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job ID :',Job_id)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Title :',Job_Title)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Company :',Job_company)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Description :',Job_jobDescription)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Posting Date :',Job_jobPostingDate)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Type :',Job_jobType)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Level :',Job_jobLevel)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Category :',Job_category)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Years of Experience :',Job_yearsOfExperience)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Org :',Job_organization)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Last Modification Date :',Job_lastModificationDate)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Location :',Job_locationEn)
                except:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Sorry ..');exit()
                ifinterested=int(input(f'\n\n[{Fore.LIGHTRED_EX}?{Fore.RESET}] Are You interested in This Job :\n\n[{Fore.LIGHTRED_EX}1{Fore.RESET}] Yes, I would like to get the job details\n[{Fore.LIGHTRED_EX}2{Fore.RESET}] Nah, I want to get another job\n\n[{Fore.LIGHTRED_EX}#{Fore.RESET}] Your choose : '))
                if ifinterested==1:
                    rq2=get(f'https://careers.stc.com.sa/routers/jobs/1.0/ej/en/public/jobs/{Job_id}?user_id=undefined',headers={'Host': 'careers.stc.com.sa','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},allow_redirects=True,verify=False)
                    if 'There was an error, Please try again later' in rq2.text:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Try Later ..');exit()
                    else:
                        try:
                            Job_d=rq2.json()['data']['jobDetails']
                            JobPurpose=Job_d['jobPurposeEn']
                            keyResponsibilities=Job_d['keyResponsibilitiesEn']
                            qualification=Job_d['qualification']
                            major=Job_d['major']
                            natureOfExperience=Job_d['natureOfExperience']
                            englishLevel=Job_d['englishLevel']
                            try:certification=Job_d['certification']
                            except:certification='Null'
                            JobCategory=Job_d['jobCategory']
                            generalManagement=Job_d['generalManagement']
                            department=Job_d['department']
                            section=Job_d['section']
                            sector=Job_d['sector']
                            
                            #print section 
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Purpose :',JobPurpose)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Title :',keyResponsibilities)
                            print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Job Qualifications :\n\n')
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Degree :',qualification)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Major :',major)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Nature Of Experience :',natureOfExperience)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job English Level :',englishLevel)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Certification :',certification)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Category :',JobCategory)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job General Management :',generalManagement)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Department :',department)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Section :',section)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Sector :',sector)
                            print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job url : https://careers.stc.com.sa/?source=TweakPY-Telegram/jobs/jobResults#/jobs/jobDescription/{Job_id}')
                        except:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Sorry ..');exit()
                else:print(f'\n\n[{Fore.LIGHTRED_EX}!{Fore.RESET}] I Will Recommend You to use Multiple Job Searcher ..');exit()
        else:exit('[!] Error ..')


    def Multiple_Job_Searcher(self):
        Keyword=input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] Job Title or Keywords : ')
        pageSize=10;page=1
        head={'Host': 'careers.stc.com.sa','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'application/json; charset=utf-8','Content-Length': '240','Origin': 'https://careers.stc.com.sa','Referer': 'https://careers.stc.com.sa/?source=TweakPY-Telegram','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'}
        try:
            rq0=post('https://careers.stc.com.sa/routers/job-alert/1.0/ej/private/job/alert',headers=head,json={"data":{"request":{"userId":f"{email}","searchKey":[],"selectedFilters":{"categories":[],"jobTypes":[{"value":"Experienced","key":"EXPERIENCED"},{"value":"Fresh Graduate","key":"FRESHER"},{"value":"Trainee","key":"TRAINEE"}]},"hiringType":"external"}}},allow_redirects=True,verify=False)
            rq1=post('https://careers.stc.com.sa/routers/jobs-search/1.0/ej/en/public/jobs/search',headers=head,json={"data":{"request":{"userId":"","searchKey":[f"{Keyword}"],"selectedFilters":{"categories":[],"jobTypes":[]},"hiringType":"external","pageNum":f"{page}","pageSize":f"{pageSize}"}}},allow_redirects=True,verify=False)
        except:pass;exit('[!] Fetal Error sorry ...')    
        if '{"data":{"jobs":[]}}' in rq1.text:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] 0 Jobs Found ..');exit('[+] We will inform You if anything new came out ...')
        elif 'paginationDetails' in rq1.text:
            try:print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}]',rq1.json()['data']["paginationDetails"]["totalRecords"],'Jobs Found !');print('\n')
            except:pass 
            try:
                t1=re.findall('"jobTitle":"(.*?)"',rq1.text)[0];t2=re.findall('"jobTitle":"(.*?)"',rq1.text)[1];t3=re.findall('"jobTitle":"(.*?)"',rq1.text)[2];t4=re.findall('"jobTitle":"(.*?)"',rq1.text)[3];t5=re.findall('"jobTitle":"(.*?)"',rq1.text)[4];t6=re.findall('"jobTitle":"(.*?)"',rq1.text)[5];t7=re.findall('"jobTitle":"(.*?)"',rq1.text)[6];t8=re.findall('"jobTitle":"(.*?)"',rq1.text)[7];t9=re.findall('"jobTitle":"(.*?)"',rq1.text)[8];t10=re.findall('"jobTitle":"(.*?)"',rq1.text)[9]
                l1=re.findall('"jobLevel":"(.*?)"',rq1.text)[0];l2=re.findall('"jobLevel":"(.*?)"',rq1.text)[1];l3=re.findall('"jobLevel":"(.*?)"',rq1.text)[2];l4=re.findall('"jobLevel":"(.*?)"',rq1.text)[3];l5=re.findall('"jobLevel":"(.*?)"',rq1.text)[4];l6=re.findall('"jobLevel":"(.*?)"',rq1.text)[5];l7=re.findall('"jobLevel":"(.*?)"',rq1.text)[6];l8=re.findall('"jobLevel":"(.*?)"',rq1.text)[7];l9=re.findall('"jobLevel":"(.*?)"',rq1.text)[8];l10=re.findall('"jobLevel":"(.*?)"',rq1.text)[9]
                y1=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[0];y2=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[1];y3=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[2];y4=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[3];y5=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[4];y6=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[5];y7=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[6];y8=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[7];y9=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[8];y10=re.findall('"yearsOfExperience":"(.*?)"',rq1.text)[9]
            except:exit('[!] Error code: M1CD1 ..')
            print(f"-------------------------------------------------------------------------------------------")
            print(f'Num |   Title      |      Levle      |      Years Experience  ')
            print(f'0   | -------------------------------------------------------------------------------------')         
            print(f'1   |{t1}\t|\t{l1}\t|\t{y1}')              
            print(f'2   |{t2}\t|\t{l2}\t|\t{y2}')     
            print(f'3   |{t3}\t|\t{l3}\t|\t{y3}')       
            print(f'4   |{t4}\t|\t{l4}\t|\t{y4}')       
            print(f'5   |{t5}\t|\t{l5}\t|\t{y5}')
            print(f'6   |{t6}\t|\t{l6}\t|\t{y6}')        
            print(f'7   |{t7}\t|\t{l7}\t|\t{y7}') 
            print(f'8   |{t8}\t|\t{l8}\t|\t{y8}')        
            print(f'9   |{t9}\t|\t{l9}\t|\t{y9}')         
            print(f'10  |{t10}\t|\t{l10}\t|\t{y10}')     
            print(f"-------------------------------------------------------------------------------------------")	
            ifinterested=int(input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] which Job are You interested in From 1 to 10 : '))
            if ifinterested==1:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[0]
            elif ifinterested==2:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[1]
            elif ifinterested==3:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[2]
            elif ifinterested==4:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[3]
            elif ifinterested==5:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[4]
            elif ifinterested==6:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[5]
            elif ifinterested==7:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[6]
            elif ifinterested==8:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[7]
            elif ifinterested==9:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[8]
            elif ifinterested==10:Job_id=re.findall('{"jobId":"(.*?)"',rq1.text)[9]
            rq2=get(f'https://careers.stc.com.sa/routers/jobs/1.0/ej/en/public/jobs/{Job_id}?user_id=undefined',headers={'Host': 'careers.stc.com.sa','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0','Accept': 'application/json, text/plain, */*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-origin','Te': 'trailers','Connection': 'close'},allow_redirects=True,verify=False)
            if 'There was an error, Please try again later' in rq2.text:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Try Later ..');exit()
            else:
                try:
                    Job_d=rq2.json()['data']['jobDetails']
                    JobPurpose=Job_d['jobPurposeEn']
                    keyResponsibilities=Job_d['keyResponsibilitiesEn']
                    qualification=Job_d['qualification']
                    major=Job_d['major']
                    natureOfExperience=Job_d['natureOfExperience']
                    englishLevel=Job_d['englishLevel']
                    try:certification=Job_d['certification']
                    except:certification='Null'
                    JobCategory=Job_d['jobCategory']
                    generalManagement=Job_d['generalManagement']
                    department=Job_d['department']
                    section=Job_d['section']
                    sector=Job_d['sector']
                    
                    #print section 
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Purpose :',JobPurpose)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Title :',keyResponsibilities)
                    print(f'[{Fore.LIGHTRED_EX}!{Fore.RESET}] Job Qualifications :\n\n')
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Degree :',qualification)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Major :',major)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Nature Of Experience :',natureOfExperience)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job English Level :',englishLevel)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Certification :',certification)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Category :',JobCategory)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job General Management :',generalManagement)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Department :',department)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Section :',section)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job Sector :',sector)
                    print(f'[{Fore.LIGHTRED_EX}+{Fore.RESET}] Job url : https://careers.stc.com.sa/?source=TweakPY-Telegram/jobs/jobResults#/jobs/jobDescription/{Job_id}')
                except:print(f'[{Fore.LIGHTRED_EX}-{Fore.RESET}] Error Sorry ..');exit()


print(f"""
     ██╗ ██████╗ ██████╗       ███████╗
     ██║██╔═══██╗██╔══██╗      ██╔════╝
     ██║██║   ██║██████╔╝█████╗███████╗
██   ██║██║   ██║██╔══██╗╚════╝╚════██║
╚█████╔╝╚██████╔╝██████╔╝      ███████║  {Fore.LIGHTRED_EX}██╗ ██╗{Fore.RESET}
 ╚════╝  ╚═════╝ ╚═════╝       ╚══════╝  {Fore.LIGHTRED_EX}╚═╝ ╚═╝{Fore.RESET}  
          By @TweakPY - @vv1ck                                                                 
""")	
print(Fore.BLUE+'--{ Looking for a job? Well, this is the place to look for it }--'+Fore.RESET)
em=input(f'\n[{Fore.LIGHTRED_EX}?{Fore.RESET}] Would You Like to Get an Email if The Job is Available [{Fore.LIGHTRED_EX}Y{Fore.RESET}-{Fore.LIGHTRED_EX}n{Fore.RESET}] : ');print('\n')
if em=='Y':email=input(f'[{Fore.LIGHTRED_EX}?{Fore.RESET}] Your Email : ');print('\n')
else:email='Null'
starter=int(input(f'\n\n[{Fore.LIGHTRED_EX}?{Fore.RESET}] Single Search or Multiple Search :\n\n[{Fore.LIGHTRED_EX}1{Fore.RESET}] Single Search\n[{Fore.LIGHTRED_EX}2{Fore.RESET}] Multiple Search\n\n[{Fore.LIGHTRED_EX}#{Fore.RESET}] Your choose : '))

if starter==1:Job(email).Single_Job_Searcher() 
else:Job(email).Multiple_Job_Searcher()
