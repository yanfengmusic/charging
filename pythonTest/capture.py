__mtime__ = '2020-02-05'

import requests
import re
import xlwt

#-------------------存储初始化----------------
workbook = xlwt.Workbook(encoding='utf-8')
sheet_name = workbook.add_sheet("capture")
sheet_head = ["工作岗位","公司名称","所在区域","工资","发布日期"]
for col in range(0, len(sheet_head)):
    sheet_name.write(0, col, sheet_head[col]) #行，列，内容

def get_webPage():
    web_url = "https://search.51job.com/list/010000%252C020000%252C030200%252C040000%252C090200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    resp = requests.get(web_url)
    resp.encoding = 'gbk'
    pages = re.findall('<span class="td">共(.*?)页，到第</span>', resp.text)[0]
    return int(pages)
line = 1
for one in range(1,get_webPage()+1):

    #-------------------模拟浏览器进行请求----------------
    web_url = f"https://search.51job.com/list/010000%252C020000%252C030200%252C040000%252C090200,000000,0000,00,9,99,%25E8%2587%25AA%25E5%258A%25A8%25E5%258C%2596%25E6%25B5%258B%25E8%25AF%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,{one}.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    resp = requests.get(web_url)
    resp.encoding = 'gbk'
    # print(resp.text)
    info = re.findall('div class="el">(.*?)</div>', resp.text, re.S)

    """
     <div class="el">
     <p class="t1 ">
         <em class="check" name="delivery_em" onclick="checkboxClick(this)"></em>
         <input class="checkbox" type="checkbox" name="delivery_jobid" value="119913867" jt="0" style="display:none">
         <span>
             <a target="_blank" title="自动化测试工程师（电商）" href="https://jobs.51job.com/shenzhen-nsq/119913867.html?s=01&amp;t=0" onmousedown="">
                 自动化测试工程师（电商）                </a>
         </span>
                                                                 </p>
     <span class="t2"><a target="_blank" title="深圳纷来电子商务有限公司" href="https://jobs.51job.com/all/co5737127.html">深圳纷来电子商务有限公司</a></span>
     <span class="t3">深圳-南山区</span>
     <span class="t4">1.2-1.6万/月</span>
     <span class="t5">02-07</span>
 </div>

     """

    for one in info:
        try:
            job_name = re.findall(' <a target="_blank" title=(.*?)href="https://jobs.51job.com',one,re.S)[0]
            sheet_name.write(line, 0, job_name)

            company_name = re.findall('<span class="t2"><a target="_blank" title=(.*?)href="https://jobs.51job',one,re.S)[0]
            sheet_name.write(line, 1, company_name)

            company_area = re.findall('<span class="t3">(.*?)</span>',one,re.S)[0]
            a = sheet_name.write(line, 2, company_area)

            job_salary = re.findall('<span class="t4">(.*?)</span>',one,re.S)[0]
            sheet_name.write(line, 3, job_salary)

            job_date= re.findall('<span class="t5">(.*?)</span>',one,re.S)[0]
            sheet_name.write(line, 4, job_date)

            line += 1
        except Exception as info:
            print(info)
        # print(job_name,company_name,company_area,job_salary,job_date)




    workbook.save('e:\\capture.xls')  # 存放到具体的磁盘路径



