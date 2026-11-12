# Nov 12: market pages (EN rewrites of noindexed thin pages + zh-Hant TW/HK)
import sys; sys.path.insert(0,'/workspace/site/scripts/nov11'); sys.path.insert(0,'/workspace/site/scripts/nov12')
from gen import ul, ol, a, table
from wl_en import VOL, TERMS, NEVER, FEES, START
PAGES=[]
def add(**k): k.setdefault('crumb',('Agencies','/white-label-agency/')); k.setdefault('crumbtxt','Home / For agencies'); PAGES.append(k)
FEELINE='Instagram $800, Facebook profile $900, Facebook Page $600 per Page, ad account $1,200, Business Portfolio $1,500, username claim $1,200 per handle, Snapchat $800, TikTok $900, YouTube $1,200'
def mk(slug,country,adj,cc,phone,biz,lang_note,report,tz,invoice,extra_rows,faq_extra,alts=None,area=None):
    rows=[('Notice language',lang_note),('Phone numbers',phone),('Business details',biz),('Time zone',tz),('If a hacked account was used to scam people',report)]+extra_rows
    add(slug=slug,alts=alts,area=area,
     title=f'White Label Account Recovery for {adj} Agencies (2026) | Unbanz',short=f'White label for {country}',
     desc=f'For agencies, resellers and social media managers in {country}: offer Instagram, Facebook, Meta ad account, TikTok, YouTube and username recovery under your own brand. Fixed USD fees, upfront, 100% refund if a case fails.',
     h1=f'White label recovery for {adj} agencies.',lede=f'Your client in {country} keeps dealing with you. Unbanz does the platform work behind your brand.',
     answer=f'<strong>Agencies in {country} can resell account recovery under their own brand: you stay the client’s only contact, and Unbanz works the case through the platform’s official routes and sends you unbranded updates.</strong> Fees are fixed per case in USD and paid upfront ({FEELINE}), with a 100% refund for any case that fails. {VOL} The platform makes the final decision; usually 3–7 days, not guaranteed.',
     cards=[('You keep the client','We never contact them.'),(f'Checks for {country}','Phone, business and notice details.'),('Volume pricing','For regular or batch partners.')],
     sections=[('how','How it works',ol(['Your client sends you the notice screenshot, the account link and the date.','You email the case to team@unbanz.com with your own reference; no client name is needed.','We confirm whether we can take it, and you pay upfront for that case.','We work it through official routes and send you unbranded updates to forward.'])),
      ('local',f'Details that matter in {country}',table(rows,('Point','What to do'))),
      ('fees','Fees and invoicing your client',FEES+f'<p>{invoice}</p>'),
      ('terms','Partner terms',TERMS),('never','What is never part of it',NEVER),('start','Start',START('your city'))],
     faqs=[(f'Can a {adj} agency resell Unbanz under its own brand?','Yes. Your client deals only with you, and Unbanz never contacts them or mentions Unbanz.'),('Do partners get volume pricing?','Yes. '+VOL),('What happens if a case fails?','That case is refunded 100%.')]+faq_extra,
     related=[('/white-label-agency/','White label for agencies'),('/white-label-recovery-services-by-platform/','Services by platform'),('/white-label-bulk-recovery-cases-for-agencies/','Sending cases in bulk')])
mk('white-label-agency-australia','Australia','Australian','AU','An Australian mobile written 04xx xxx xxx is entered as +61 4xx xxx xxx, without the leading zero.','Have the ABN, the registered business name and a website or email on the business domain ready; enter the name exactly as it appears on the ABN Lookup record.','Notices appear in English, so screenshots can be sent as they are.','Report it to ReportCyber (cyber.gov.au) and note the reference number for your client’s records.','Updates are dated so they make sense across time zones; Australia runs AEST/AEDT in the east and AWST in the west.','Unbanz bills you in USD. What you charge your client, in AUD and including any GST, is your decision; ask your accountant how to treat it.',
   [('Ad account billing','If the ad account is billed in AUD and the card was recently changed, mention it in the case; billing changes are a common trigger for ad account restrictions.')],
   [('Do you work with Australian time zones?','Yes. Every update is dated and you can forward it whenever suits your client.')],area=['AU'])
mk('white-label-agency-uae','the UAE','UAE','AE','A UAE mobile written 05x xxx xxxx is entered as +971 5x xxx xxxx, without the leading zero.','Have the trade licence (mainland or free zone) and the business name in English exactly as printed on it. See '+a('/meta-business-verification-uae-trade-licence/','Meta verification with a UAE trade licence')+'.','Notices may appear in Arabic or English. Send the screenshot as it is; no translation is needed.','Report it to the police through the eCrime platform (ecrime.ae) and keep the reference.','The UAE is UTC+4 all year.','Unbanz bills you in USD. What you charge your client, in AED and including any VAT, is your decision.',
   [('Business Portfolios with several brands','Many UAE groups run several trade names in one portfolio. List every brand and licence in the case so the right documents are used.')],
   [('Can you handle Business Portfolios for UAE groups?','Yes. Business Portfolio cases are $1,500, upfront, with a 100% refund if it fails.')],area=['AE'])
mk('white-label-agency-taiwan','Taiwan','Taiwanese','TW','A Taiwanese mobile written 09xx-xxx-xxx is entered as +886 9xx xxx xxx, without the leading zero.','Have the company name and the 8-digit Unified Business Number (統一編號), plus a website or email on the business domain. The name entered must match the registration.','Meta and TikTok notices often appear in Traditional Chinese. Send the screenshot as it is; no translation is needed.','Report it to the 165 anti-fraud hotline and keep the record for your client.','Taiwan is UTC+8 all year. Updates are dated so you can forward them the next morning.','Unbanz bills you in USD. What you charge your client in TWD is your decision.',
   [('Client chats','Many Taiwanese clients talk to their agency on LINE. Keep that conversation with your client; send us the case by email.')],
   [('Is there a Traditional Chinese version of this page?','Yes: '+a('/zh-tw/white-label-agency/','台灣代理商白牌帳號恢復')+'.')],alts={'en':'white-label-agency-taiwan','zh-tw':'zh-tw/white-label-agency'},area=['TW'])
mk('white-label-agency-hong-kong','Hong Kong','Hong Kong','HK','A Hong Kong number has 8 digits and is entered as +852 xxxx xxxx.','Have the company name as shown on the Business Registration Certificate (BR) and, for a limited company, the Certificate of Incorporation, plus a website or email on the business domain.','Notices may appear in Traditional Chinese or English. Send the screenshot as it is; no translation is needed.','Report it to the Hong Kong Police e-Report Centre and keep the reference.','Hong Kong is UTC+8 all year.','Unbanz bills you in USD. What you charge your client in HKD is your decision.',
   [('Brands across Hong Kong and the mainland','If one client runs Hong Kong and other regional accounts, list every account and Page in the case so nothing is missed.')],
   [('Is there a Traditional Chinese version of this page?','Yes: '+a('/zh-hk/white-label-agency/','香港代理商白牌帳戶恢復')+'.')],alts={'en':'white-label-agency-hong-kong','zh-hk':'zh-hk/white-label-agency'},area=['HK'])

# ---- zh-Hant pages ----
def zh(lang,slug,place,acct,page,adacct,phone,biz,report,lede_extra,alts,area):
    VOLZ='固定或大量送件的合作夥伴可享量價，條件在開始前以書面約定；我們不公開具體數字。'
    FEEZ=table([('Instagram '+acct,'$800'),('Facebook 個人'+acct,'$900'),('Facebook '+page,'每個 $600'),('Instagram 或 Facebook '+adacct,'$1,200'),('Meta Business Portfolio','$1,500'),('用戶名稱申請','每個 $1,200'),('Snapchat '+acct,'$800'),('TikTok '+acct,'$900'),('YouTube 頻道','$1,200')],('項目','費用（美元，每件）'))
    add(lang=lang,slug=slug,alts=alts,area=area,crumb=('代理商合作','/white-label-agency/'),crumbtxt='Unbanz / 代理商合作',
     title=f'{place}代理商白牌{acct}恢復服務（Instagram、Facebook、TikTok）| Unbanz',short=f'{place}白牌{acct}恢復',
     desc=f'給{place}的行銷代理商、社群經營團隊與{acct}救援業者：以你自己的品牌提供 Instagram、Facebook、{adacct}、TikTok、YouTube {acct}恢復與用戶名稱申請，Unbanz 在幕後處理。每件固定費用、預付，案件失敗 100% 退款。',
     h1=f'{place}代理商的白牌{acct}恢復。',lede=f'客戶的 Instagram、Facebook 或{adacct}出問題時，你繼續當客戶唯一的窗口，平台端的工作交給 Unbanz。{lede_extra}',
     answer=f'<strong>白牌（white label）{acct}恢復是指：你的公司以自己的品牌接案，客戶只和你聯絡；Unbanz 在幕後透過平台的官方申訴管道處理案件，並把不帶 Unbanz 名稱的進度報告交給你。</strong>費用以美元計、每件固定、預付：Instagram $800、Facebook 個人{acct} $900、Facebook {page}每個 $600、{adacct} $1,200、Business Portfolio $1,500、用戶名稱每個 $1,200、Snapchat $800、TikTok $900、YouTube 頻道 $1,200；案件失敗即 100% 退款。{VOLZ}最終由平台決定，通常需要 3–7 天，時程不保證。',
     cards=[('你的品牌','客戶只認識你，我們不會聯絡客戶。'),('官方管道','只透過平台的申訴與審查流程。'),('量價','固定或大量送件的合作夥伴適用。')],
     sections=[('how','合作流程',ol(['客戶把完整的通知截圖、帳號連結與日期交給你。',f'你用 Email 把案件寄到 <a href="mailto:team@unbanz.com">team@unbanz.com</a>，附上你自己的案件編號，不需要提供客戶姓名。','我們先評估能否處理；確認接案後，該案件費用預付。','我們透過官方管道處理，並寄給你不含 Unbanz 名稱的進度報告，你可以直接轉給客戶，或貼進自己的報告格式。'])),
      ('local',f'{place}客戶要注意的細節',table([('通知語言','Meta 與 TikTok 的通知常以繁體中文顯示，截圖原樣傳來即可，不需要翻譯。'),('電話號碼',phone),('公司資料',biz),('時區',f'{place}為 UTC+8，每份進度報告都會註明日期。'),('帳號被盜後被拿去詐騙',report)],('項目','說明'))),
      ('prepare','送件前請準備',ul(['帳號連結或用戶名稱，以及帳號綁定的 Email 與電話。','完整、未裁切的通知截圖，以及出現的日期。','發生了什麼：被盜、停用、停權、廣告受限，或想申請的用戶名稱。','客戶同意由你與 Unbanz 處理這個帳號。','絕對不要向客戶索取密碼或登入驗證碼。'])),
      ('fees','費用與合作條件',FEEZ+ul(['每件預付；案件失敗，該件 100% 退款。',VOLZ,'你的公司有專屬聯絡窗口：team@unbanz.com，並使用你自己的案件編號。','進度報告不含 Unbanz 名稱或標誌，可直接轉寄。','你向客戶收取多少費用，由你決定。'])),
      ('never','我們不做的事',ul(['不索取密碼或登入驗證碼。','不買賣、不出租帳號。','不做假檢舉或大量檢舉。','不承諾結果：最終由平台決定。'])),
      ('start','開始合作',f'<p>寄信到 <a href="mailto:team@unbanz.com?subject=White%20label%20partner">team@unbanz.com</a>，告訴我們你的公司名稱、客戶主要使用的平台，以及每月大約會有多少案件。第一件案件開始前，我們會以書面回覆合作條件。Email 往來以英文進行；客戶的中文截圖不需要翻譯。</p>')],
     faqs=[('客戶會知道 Unbanz 嗎？','不會。我們不會聯絡你的客戶，寄給你的進度報告也不含 Unbanz 名稱或標誌。'),('大量案件有比較好的價格嗎？','有。'+VOLZ),('案件失敗怎麼辦？','該案件 100% 退款。'),('需要客戶的密碼嗎？','不需要。我們從不索取密碼或登入驗證碼。')],
     related=[('/white-label-agency/','White label for agencies (English)'),('/white-label-recovery-services-by-platform/','Services by platform (English)'),(f'/{alts["en"]}/',f'{place} page in English')])
zh('zh-tw','zh-tw/white-label-agency','台灣','帳號','粉絲專頁','廣告帳號','台灣手機 09xx-xxx-xxx 以國際格式填寫為 +886 9xx xxx xxx（去掉開頭的 0）。','若平台要求證明商家真實存在，請準備公司名稱、8 碼統一編號，以及網站或公司網域的 Email；名稱須與登記資料一致。','請撥打 165 反詐騙諮詢專線報案，並保留紀錄給客戶。','很多台灣客戶習慣用 LINE 和代理商聯絡，這段對話留在你和客戶之間即可。',{'en':'white-label-agency-taiwan','zh-tw':'zh-tw/white-label-agency'},['TW'])
zh('zh-hk','zh-hk/white-label-agency','香港','帳戶','專頁','廣告帳戶','香港電話為 8 位數字，以國際格式填寫為 +852 xxxx xxxx。','若平台要求證明商家真實存在，請準備商業登記證（BR）上的公司名稱；有限公司另備公司註冊證明書，以及網站或公司網域的 Email。','請透過香港警務處網上報案中心報案，並保留報案編號。','',{'en':'white-label-agency-hong-kong','zh-hk':'zh-hk/white-label-agency'},['HK'])
