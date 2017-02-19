'''
         Scraping web pages from amazon using python beautifulSoup

        Author : Avinash Vootkuri
'''

from urllib2 import urlopen
from urllib2 import HTTPError
import urllib2
import time
import re
from bs4 import BeautifulSoup

amazonPageUrls = [
					"http://www.amazon.com/dp/B00U3FPN4U/",
					"http://www.amazon.com/dp/B019WAQMVY/",
					"http://www.amazon.com/gp/product/B014X4UAUI/",
					"http://www.amazon.com/dp/B00XJZ52O2/",
					"http://www.amazon.com/dp/B00W1EHEZW",
					"http://www.amazon.com/dp/B00B3X73EE",
					"http://www.amazon.com/Samsung-2-5-Inch-Internal-MZ-75E250B-AM/dp/B00OAJ412U/",
					"http://www.amazon.com/Rosewill-Anti-Static-Components-RTK-002-Yellow/dp/B004N8ZQKY/",
					"http://www.amazon.com/Arctic-Silver-High-Density-Polysynthetic-Compound/dp/B000OGX5AM/",
					"http://www.amazon.com/AMD-FD6300WMHKBOX-FX-6300-Processor-Edition/dp/B009O7YORK/",
					"http://www.amazon.com/EVGA-Continuous-Warranty-Supply-100-W1-0500-KR/dp/B00H33SFJU/",
					"http://www.amazon.com/Blue-Desktop-Hard-Disk-Drive/dp/B0088PUEPK/",
					"http://www.amazon.com/AmazonBasics-HDMI-DVI-Adapter-Cable/dp/B00L3KNZZ8/",
					"http://www.amazon.com/Logitech-Wireless-Combo-Mk520-Keyboard/dp/B003VANO7C/",
					"http://www.amazon.com/Samsung-Simple-Monitor-S24D300H-Glossy/dp/B00M2UIWKQ/"
				]
print ("===========================================================================") 
print ("Extracting Information from Provided links from Amazon Site...")
print
print

i=0

while True:
	try:
		htmlPage=urlopen(amazonPageUrls[i])
		soup = BeautifulSoup(htmlPage)

		#extracting Product Name
		productNameHTML = str(soup.find(id="productTitle"))
		productName = re.sub("(<[^>]+>)", "", productNameHTML)

		#extracting rating
		starsHTML = str(soup.find(id="reviewStarsLinkedCustomerReviews"))
		stars = re.sub("(<[^>]+>)", "", starsHTML)

		#extracting Price
		priceHTML = str(soup.find(id="priceblock_ourprice"))
		price = re.sub("(<[^>]+>)", "", priceHTML)

		#extracting Availability Info
		availabilityHTML = str(soup.find(id="availability"))
		availability = re.sub("(<[^>]+>)", "", availabilityHTML)

		#extracting Reviews Div
		reviewsCompleteHTML = soup.find(id="revMHRL")
		reviewsArrayHTML = reviewsCompleteHTML.findAll("div", "a-icon-row a-spacing-none")
		reviewersArrayHTML = reviewsCompleteHTML.findAll("span", "a-color-secondary")
		reviewersDescriptionArrayHTML = reviewsCompleteHTML.findAll("div", "a-section celwidget")
		#print reviewsArrayHTML




		productName = re.sub("([\n]+)", "", productName).strip();
		stars = re.sub("([\n]+)", "", stars).strip();
		price = re.sub("([\n]+)", "", price).strip();
		availability = re.sub("([\n]+)", "", availability).strip();

		print ("Extracting Page Number : " + str(i + 1))
		print ("Extracting Url : " + amazonPageUrls[i])
		print ("Product Name : " + productName)
		print ("Rating : " + stars)
		print ("Price : " + price)
		print ("Availability : " + availability)

		print

		if(len(reviewsArrayHTML) > 0):
			print ("******************Top Reviews from Customers**********************")

		#print reviewersDescriptionArrayHTML
		#break

		j = 0
		while j < (len(reviewsArrayHTML)):
			print ("Top " + str(j + 1) + " Customer Review : ")
			print ("Reviewer Name : " + str(re.sub("(<[^>]+>)", "", str(reviewersDescriptionArrayHTML[j].find("a","noTextDecoration")))))
			print ("Reviewer Date : " + str(re.sub("(<[^>]+>)", "", str(reviewersDescriptionArrayHTML[j].findAll("span","a-color-secondary")[2]))))
			print ("Review Title : " + str(re.sub("(<[^>]+>)", "", str(reviewersDescriptionArrayHTML[j].find("span","a-size-base a-text-bold")))))
			print ("Reviewer Rating : " + str(re.sub("(<[^>]+>)", "", str(reviewersDescriptionArrayHTML[j].find("a","a-link-normal a-text-normal a-color-base")))))
			print ("Review Description : " + str(re.sub("(<[^>]+>)", "", str(reviewersDescriptionArrayHTML[j].find("div","a-section")))))
			print
			j= j + 1

		print ("===========================================================================")
		print ("===========================================================================")


		i = i + 1
		if i==15:
			break
	except urllib2.HTTPError:
		time.sleep(1)


print ("Extraction Completed Successfully")

#htmlPage=urllib2.urlopen("http://www.amazon.com/gp/product/B00THKEKEQ/ref=s9_ri_gw_g421_i1_r?ie=UTF8&fpl=fresh&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=desktop-2&pf_rd_r=1NC350RX12QJWWJBSBA1&pf_rd_t=36701&pf_rd_p=2091268582&pf_rd_i=desktop")
