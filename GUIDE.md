# Keyword Relevance Grading Guide

Version 1.1 · 2026-10-21

You grade search keywords against a seed keyword. A similar-keywords model returned each keyword for its seed; your grade says how close the keyword really is to the seed, on six levels. The grades become training data that teach the model which keywords to return for a seed, and in what order.

Everything you need is in this guide. Grade each batch with this guide and the batch alone: no earlier batches, other files or notes. The one thing to look up is meaning: when you're unsure what a seed or keyword means, search the web for it before grading (section 9).

**Contents:** 1 The data · 2 The six levels · 3 Read the seed first · 4 Decide in this order · 5 Levels 1–3 by kind of keyword · 6 Levels 4–6 · 7 By type of seed · 8 Fine lines · 9 Keyword forms · 10 Worked seeds · 11 Contrast pairs · 12 Mistakes to avoid · 13 Consistency · 14 Output format · 15 Before you submit · Appendix

---

## 1. The data

- Seeds and keywords are real searches made in Iran, mostly in Persian. Some mix in English words, brand names, model codes, numbers or typos.
- A batch shows one or more seeds. Under each seed is a numbered list of keywords to grade. A seed may also show a category or intent: treat those as hints about the seed's need, never as a filter.
- The lists are not cleaned. Some seeds have mostly close keywords, others mostly noise. There is no expected mix of levels: grade what you see.
- You never see the model's score, the keyword's rank, its website or its search volume, and none of them matter for the grade.

## 2. The six levels

| Level | Found? | Definition | Test question | Example (seed → keyword) |
|---|---|---|---|---|
| **1** | Yes, first | **Same thing, same need.** The seed reworded or narrowed, a comparison about it, or something its searcher needs as part of the same goal | Is this the seed itself, said differently or more precisely, or part of the same goal? | «کراتین مو» → «کراتین مو مشهد» (keratin hair treatment, in Mashhad) |
| **2** | Yes | **Same thing, wider or sideways.** One step broader, a close rival, the same need in another place, an accessory or add-on, a side task on the same thing | Is it the same thing, but wider, a substitute, somewhere else, an add-on or a side task? | «خرید تلویزیون شیائومی» → «تلویزیون سامسونگ» (a rival brand) |
| **3** | Yes, last | **Another thing in the same field.** A neighbor product or service, a distant rival, the same brand's other products, a repair or other paid service around it, a factory, the whole field | Is it a different thing that the same kind of person deals with around this need? | «شمش طلا» → «دستبند طلا ظریف دخترانه» (a gold bracelet, for a gold bar seed) |
| **4** | No | **Linked only on the surface.** A shared word, part of a word, a similar spelling or sound, and no relation at levels 1–3 | Take away the shared word or spelling: is anything left that connects them? If not → 4 | «یخچال» → «یخچال طبیعی» (a glacier, for a fridge seed) |
| **5** | No | **No link at all.** Nothing in the keyword's text links it to the seed, and there is no relation | Does it share no word, spelling or relation with the seed? | «قیمت 206» → «صفر تا صد خیاطی» (learning to sew, for a car price seed) |
| **6** | No | **No topic.** A generic word or broken text, whatever the seed | Is the keyword empty of meaning on its own? | «قیمت», «آنلاین», «گگ» |

Levels 1–3 are keywords the model should find, level 1 ranked first. Levels 4–6 are keywords it should not find, and the number says why. The short names niche (1), topical (2), journey (3), look-alike (4), unrelated (5) and junk (6) are only labels; always grade by the definitions.

Two ideas carry the whole scale:
- **The need decides, not the words.** A keyword can share no word with the seed and be level 1, or share every word and be level 4.
- **Narrower stays close, wider moves out.** Adding detail to the seed keeps its need (1). Dropping detail widens it (2). Moving to another thing in the field moves it further (3).

## 3. Read the seed first

Before you grade a seed's list, settle three things.

**1. The need.** What does the person searching the seed want to do? Most seeds are one of these types:

| Seed type | The need | Examples |
|---|---|---|
| Product | Choose and buy it | «خرید لپ تاپ», «اسپیکر», «سرخ کن بدون روغن» |
| Service | Get it done by someone | «کراتین مو», «لوله بازکنی», «وکیل ملکی» |
| Condition or problem | Understand it and treat it | «درمان میگرن», «واریس پا» |
| Topic or decision | Learn about it, decide, act on it | «مهندسی کامپیوتر», «ترک سیگار», «هزینه زندگی آلمان» |
| Trip or stay | Travel to a place, stay there | «تور قشم», «اجاره سوئیت در مشهد» |
| Local business | Find a place to go in a city | «فست فود تهران», «تالار عروسی» |
| Activity | Do something yourself | «چاپ لیوان», «حذف پس زمینه عکس» |
| Animal or thing you keep | Get one and care for it | «مرغ عشق», «سگ سرابی» |
| Investment or money | Buy, hold or follow an asset | «شمش طلا» |

Words like «خرید», «فروش», «قیمت», «بهترین», «ارزان», «لیست», «انواع», «مدل», «نحوه», «روش» and «چیست» only shade the need. A keyword about the same thing for the same need is level 1 whichever of them it uses: «قیمت لوله بازکنی» is level 1 for «لوله بازکنی».

**2. The core and its qualifiers.** Split the seed into its core (the product, service, condition, activity or subject) and its qualifiers (brand, model, type, size, material, city or area, time, audience). In «خرید تلویزیون شیائومی» the core is the TV and the qualifier is the brand Xiaomi. A keyword that adds qualifiers narrows the seed; one that drops a qualifier widens it.

**3. Its meanings.** Every common meaning of the seed counts, unless the seed's own words pick one. «برنج» covers both rice and brass, so a keyword about either meaning is graded against that meaning; «برنج ایرانی» is only rice. A keyword about a meaning the seed doesn't have shares only a word with it: level 4.

## 4. Decide in this order

1. **No topic first.** Read the keyword alone. If it has no topic of its own (a generic word, a page fragment, broken text) → **6**, even when it is part of the seed: «قیمت» is 6 for «قیمت پمپ شناور».
2. **Same thing, same need?** → **1**.
3. **Same thing, wider or sideways?** → **2**.
4. **Another thing in the seed's field, around the same need?** → **3**.
5. **Not found:** does the keyword share a word, part of a word, a spelling or a sound with the seed? → **4**. Nothing in common → **5**.

Take the first step that fits. Two consequences:
- A keyword with a real relation is never 4, even when it shares words: «تعمیر اسپیکر» shares «اسپیکر» with «اسپیکر» and is 3, not 4.
- A keyword with no real relation that shares a word is always 4, never 5.

When two levels fit equally well, give both, first choice first (section 14). Keep this for real doubt.

## 5. Levels 1–3 by kind of keyword

Find the keyword's kind; the table gives its level. All examples are graded: follow them.

### Level 1: same thing, same need

| Kind | Examples (seed → keyword) |
|---|---|
| The seed reworded: a synonym, another spelling or word order, singular or plural, or the same need with «قیمت», «خرید», «بهترین», «روش», «لیست» or «مدل» | «لوله بازکنی» → «قیمت لوله بازکنی» · «ترک سیگار» → «روش ترک سیگار» · «کراتین مو» → «قیمت کراتین مو زنانه» |
| Narrowed by brand, model, type, size, material, audience, condition (new or used) or payment | «سرخ کن بدون روغن» → «سرخ کن بدون روغن شیائومی» · «خرید تلویزیون شیائومی» → «خرید تلویزیون شیائومی ۴۳ اینچ» · «قیمت پمپ شناور» → «قیمت پمپ شناور 6 اینچ» · «چاپ لیوان» → «چاپ روی لیوان شیشه ای» · «مرغ عشق» → «مرغ عشق ابلق» · «خرید لپ تاپ» → «لپ تاپ استوک» (used laptops) |
| Narrowed to the vehicle, device or person it is for | «باتری خودرو» → «باتری پراید» (a battery for the Pride car) |
| Narrowed by time: a year, a season, today | «تور قشم» → «تور قشم نوروز ۱۴۰۲» |
| Narrowed by city, area or a spot | «وکیل ملکی» → «وکیل ملکی شیراز» · «تالار عروسی» → «تالار عروسی غرب تهران» · «فست فود تهران» → «فست فود شرق تهران» · «هزینه زندگی آلمان» → «هزینه زندگی در برلین» · «کراتین مو» → «کراتین مو مشهد» |
| Narrowed by where to get it: the seed plus a shop, clinic or provider | «ترک سیگار» → «کلینیک ترک سیگار تبریز» · «خرید لپ تاپ» → «لپ تاپ core i5 دیجی کالا» |
| Bought in bulk: the seed's item wholesale | «خرید دستکش بوکس» → «خرید عمده دستکش بوکس» |
| Types of the seed itself | «سرخ کن بدون روغن» → «انواع سرخ کن بدون روغن» |
| A comparison or buy-or-not question about the seed | «شمش طلا» → «شمش بهتره یا سکه» (bar or coin?) · «اسپیکر» → «ساندبار یا اسپیکر» |
| Information that serves the need: what it is, how it works, quality, features, specs, reviews, symptoms, causes, benefits, lifespan | «درمان میگرن» → «علائم میگرن» · «مرغ عشق» → «عمر مرغ عشق» · «خرید تلویزیون شیائومی» → «کیفیت تلویزیون های شیائومی» |
| A step of the same goal: the doctor or treatment for a condition, aftercare after a service, keeping or training an animal you keep, the tool for an activity | «درمان میگرن» → «دکتر متخصص میگرن» · «کراتین مو» → «مراقبت بعد از کراتین مو» · «سگ سرابی» → «تربیت سگ سرابی» · «چاپ لیوان» → «دستگاه چاپ لیوان» |
| What the seed is for or leads to: the event a venue hosts, the sights a tour visits, the job market a field of study leads to | «تالار عروسی» → «جشن عروسی ایرانی» · «تور قشم» → «جاهای دیدنی قشم» · «مهندسی کامپیوتر» → «بازار کار مهندسی کامپیوتر» |
| A wording that can mean the seed's need, read that way | «لوله بازکنی» → «نیازمند لوله کش» (read as "I need a plumber", not as a job ad) |

### Level 2: same thing, wider or sideways

| Kind | Examples (seed → keyword) |
|---|---|
| One step broader: the seed without one qualifier, or its parent category | «خرید تلویزیون شیائومی» → «خرید تلویزیون» · «وکیل ملکی» → «انواع وکیل» · «تور قشم» → «انواع تور» · «چاپ لیوان» → «انواع چاپ» · «هزینه زندگی آلمان» → «هزینه زندگی در اروپا» |
| The seed's brand or destination alone, when the seed is that brand plus a product, or that place plus a trip | «تلویزیون سامسونگ» → «سامسونگ» · «تور قشم» → «قشم» |
| A close rival: another brand, model, type, breed or variety of the same kind of thing, or the same kind of problem | «خرید تلویزیون شیائومی» → «تلویزیون سامسونگ» · «شمش طلا» → «قیمت شمش نقره» · «مرغ عشق» → «مرغ قناری» · «خرید دستکش بوکس» → «دستکش کاراته» · «اجاره سوئیت در مشهد» → «اجاره ویلا در مشهد» · «درمان میگرن» → «سردرد تنشی چیست» · «ترک سیگار» → «ترک قلیان» · «لوله بازکنی» → «قیمت تخلیه چاه» |
| The same need in another city or country | «فست فود تهران» → «فست فود شیراز» · «اجاره سوئیت در مشهد» → «اجاره سوئیت تهران» |
| An accessory, part, supply or add-on made for the seed | «سرخ کن بدون روغن» → «توری سرخ کن» · «اسپیکر» → «پایه اسپیکر خانگی» · «خرید تلویزیون شیائومی» → «کنترل تلویزیون شیائومی» · «تالار عروسی» → «قیمت منو تالار عروسی» (the hall's catering menu) |
| A close complement: something used with the seed, or the setup it is part of | «اسپیکر» → «سیستم صوتی خانگی» · «مهندسی کامپیوتر» → «آموزشگاه کامپیوتر» |
| A side task on the same thing: installing it (by anyone), setting it up, using it, converting it, diagnosing a fault | «کولر گازی» → «نصب کولر گازی» · «گچبری پیش ساخته» → «نصاب گچبری پیش ساخته» · «قیمت پمپ شناور» → «علت امپر کشیدن پمپ شناور» |
| The provider's side: training to provide the seed's service, careers in the seed's own field | «کاشت ابرو» → «آموزش کاشت ابرو» · «مهندسی کامپیوتر» → «استخدام مهندس کامپیوتر» |
| Background information: history, the wider market behind it, news | «فست فود تهران» → «تاریخچه فست فود» · «شمش طلا» → «انس طلا» (the world gold price) |
| Where to buy it: a store, marketplace, dealer, exchange or agency that sells it | «قیمت پمپ شناور» → «نمایندگی پمپیران» (a pump brand's dealer) · «خرید لپ تاپ» → «دیجی کالا» (an online store) |
| A similar kind of place in the same city, for a local business | «فست فود تهران» → «فود کورت تهران» |

### Level 3: another thing in the same field

| Kind | Examples (seed → keyword) |
|---|---|
| A neighbor: another product or service in the seed's field, for the same kind of customer | «شمش طلا» → «دستبند طلا ظریف دخترانه» · «تالار عروسی» → «سالن میکاپ عروس» · «درمان میگرن» → «تشنج میوکلونیک» (another neurological condition) · «وکیل ملکی» → «محاسبه حق کمیسیون املاک» · «وکیل ملکی» → «قرارداد وکیل و موکل» (lawyer contracts in general) · «هاست» → «طراحی سایت تهران وب داران» |
| A distant rival: a different product, service or procedure that only shares the category | «کراتین مو» → «بوتاکس مو» · «چاپ لیوان» → «قیمت چاپ بنر» |
| A repair or other paid service around a product, or a separate cost around the need | «اسپیکر» → «تعمیر اسپیکر» · «باتری خودرو» → «هزینه شارژ باتری ماشین» · «قیمت پمپ شناور» → «هزینه حفر چاه آب» · «هزینه زندگی آلمان» → «هزینه مهاجرت به آلمان» |
| Making it: a factory, production line or production machine | «باتری خودرو» → «کارخانه تولید باتری خودرو» |
| Opening or renting a business around it | «فست فود تهران» → «اجاره مغازه فست فود در تهران» |
| The same brand's other products | «خرید تلویزیون شیائومی» → «گوشی شیائومی» |
| A brand alone, when the seed names no brand | «خرید تلویزیون» → «سامسونگ» |
| Getting to the destination, or another need of the same trip | «اجاره سوئیت در مشهد» → «بلیط چارتر تهران مشهد» · «تور قشم» → «بلیط اتوبوس به قشم» |
| The whole field: more than one step broader | «خرید تلویزیون شیائومی» → «کالای دیجیتال» |

## 6. Levels 4–6

Use these only when levels 1–3 all fail.

### Level 6: no topic

Judged on the keyword alone, whatever the seed.
- Generic words that mean nothing until something is attached to them: «قیمت», «خرید», «فروش», «آنلاین», «بهترین», «ارزان», «جدید», «سایت», «لیست», «انواع», «درمان», «زنانه», «قیمت روز».
- Page and site fragments: «این صفحه», «لینک منبع», «درباره ما», «تماس بگیرید».
- Broken or cut-off text, a stray letter or number, a string you can't read as anything: «گگ».

Not level 6: a word with a subject of its own, however short, such as «پمپ», «تور», «هتل», «تهران» or «سامسونگ». Grade those by their relation to the seed.

### Level 4: linked only on the surface

The keyword shares a word, part of a word, a spelling or a sound with the seed, but has no relation at levels 1–3. Take away the shared part and nothing connects them.

| Kind | Examples (seed → keyword) |
|---|---|
| A shared word in another sense | «یخچال» → «یخچال طبیعی» (a glacier) · «ماشین ظرفشویی» → «سینک ظرفشویی ارزان» (a kitchen sink) · «سرویس پکیج» → «پکیج آموزشی اکسل» (an Excel course bundle) · «ساعت هواوی» → «تنظیم ساعت گوشی هواوی» (setting the clock on a Huawei phone) · «گچبری پیش ساخته» → «گچ خیاطی» (tailor's chalk) |
| Part of a word, or a similar spelling or sound | «کت تک» → «بهترین کتونی» (sneakers) · «هاست» → «هاستل» (a hostel) · «تعمیر لباسشویی» → «خشکشویی لباس» (dry cleaning) · «کراتین مو» → «کراتین بدنسازی» (creatine for bodybuilding) |
| The same word in the same sense, but another need, even the opposite one | «ترک سیگار» → «قیمت سیگار عمده» (wholesale cigarette prices) · «هزینه زندگی آلمان» → «اقتصاد آلمان» (Germany's economy) · «چاپ لیوان» → «کاردستی با لیوان کاغذی» (crafts with paper cups) · «سرخ کن بدون روغن» → «ظرف روغن مایع» (a cooking oil container) · «لوله بازکنی» → «لوله گالوانیزه» (galvanized pipe) · «تبلیغات مترو» → «نقشه مترو تهران» (the metro map) |
| The seed's words mixed into a different need | «خرید تلویزیون شیائومی» → «گوشی شیائومی به تلویزیون» (connecting a Xiaomi phone to a TV) · «قیمت 206» → «قیمت پر قو» (the price of down feathers) |
| A job at a company that only shares a word | «قیمت پمپ شناور» → «استخدام اطلس پمپ سپاهان» |
| Something else in the same place | «هتل های شیراز» → «دانشگاه شیراز» · «فست فود تهران» → «دانشگاه تهران» |

### Level 5: no link at all

Nothing in the keyword's text links it to the seed, and there is no relation:
- «قیمت 206» → «صفر تا صد خیاطی» (learning to sew)
- «هاست» → «چک لیست کمپینگ» (a camping checklist)
- «گچبری پیش ساخته» → «دوبل برگر چیست» (what a double burger is)
- «سونا و جکوزی» → «استخراج طلا به روش قدیمی» (old ways of extracting gold)

If the text shares nothing with the seed, the keyword is 5, even when you can guess why the model matched it.

## 7. By type of seed

The same kind of keyword can land differently depending on what the seed's searcher wants. For each seed type, this is where the common keywords go.

**Product seeds (choose and buy)**
- 1: the product narrowed (brand, model, size, used, wholesale), its price, specs, reviews and quality, comparisons, the product at a named store.
- 2: one step broader, rival brands and types, accessories and parts, installing, setting up or using it, diagnosing a fault, a store or dealer that sells it.
- 3: repair and other paid services, neighbor products, the same brand's other products, factories, the whole field.
- Seed «اسپیکر»: «ساندبار یا اسپیکر» 1 · «پایه اسپیکر خانگی» 2 · «سیستم صوتی خانگی» 2 · «تعمیر اسپیکر» 3.

**Service seeds (get it done)**
- 1: the service narrowed (city, type, audience), its cost, what it involves, preparation, aftercare, results and side effects, the provider.
- 2: one step broader, close rival services, the same service in another city, training to provide it, careers in it.
- 3: other services the same customer may need, distant rivals, separate costs.
- When the seed is itself a repair or upkeep service («تعمیر لباسشویی», «سرویس پکیج»), its cost and providers are 1, the same service for another appliance is 2 («تعمیر ظرفشویی» for «تعمیر لباسشویی»), and buying the appliance is 3.
- Seed «کراتین مو»: «کراتین مو مشهد» 1 · «مراقبت بعد از کراتین مو» 1 · «آموزش کراتین مو» 2 · «بوتاکس مو» 3 · «کراتین بدنسازی» 4.

**Condition seeds (understand and treat)**
- 1: symptoms, causes, tests, treatments, medicines, doctors and clinics for it, the condition narrowed (type, body part, group of people).
- 2: a close related condition (another kind of the same problem), one step broader, background.
- 3: other conditions in the same area of medicine.
- Seed «درمان میگرن»: «علائم میگرن» 1 · «دکتر متخصص میگرن» 1 · «سردرد تنشی چیست» 2 · «تشنج میوکلونیک» 3 · «درمان» 6.

**Topic and decision seeds (learn, decide, act)**
- 1: what it is, how to do it, its methods, its reasons and outcomes, providers that help.
- 2: close rival topics, careers in it, background.
- 3: separate steps or costs around it, other topics in the field.
- When the seed is a subject to learn («زبان آلمانی»), «آموزش …» of it is the same need: 1. When the seed is a service that customers buy («کاشت ابرو»), «آموزش …» trains people to provide it: 2.
- Seed «ترک سیگار»: «روش ترک سیگار» 1 · «کلینیک ترک سیگار تبریز» 1 · «ترک قلیان» 2 · «قیمت سیگار عمده» 4.

**Trip and stay seeds (the place is the point)**
- 1: the trip or stay narrowed (dates, type, an area or landmark), and what the seed itself includes (the sights a tour visits).
- 2: another kind of stay or tour in the same place, the same trip to another place, the place alone, one step broader, an agency that sells it.
- 3: getting there, and other needs of the same trip (sights, when the seed is only a place to stay).
- 4: things in the same place that serve no trip need.
- Seed «تور قشم»: «تور قشم نوروز ۱۴۰۲» 1 · «جاهای دیدنی قشم» 1 · «انواع تور» 2 · «قشم» 2 · «بلیط اتوبوس به قشم» 3.

**Moving or studying abroad (the country is the point)**
- 1: steps of the same plan (the visa, admission or residency it needs), the plan narrowed to a city.
- 2: the same plan for another country, one step broader.
- 3: separate costs and steps around the move.
- 4: facts about the country that serve no step of the plan.
- Seed «هزینه زندگی آلمان»: «هزینه زندگی در برلین» 1 · «هزینه زندگی در اروپا» 2 · «هزینه مهاجرت به آلمان» 3 · «اقتصاد آلمان» 4.

**Local business seeds (a place to go)**
- 1: the business narrowed (area, type), its prices, the event or purpose it serves.
- 2: the same business in another city, the business without its city, add-ons it sells, a similar kind of place in the same city.
- 3: other businesses the same customer uses for the same occasion, opening such a business.
- 4: anything else that only shares the city.
- Seed «فست فود تهران»: «فست فود شرق تهران» 1 · «فست فود شیراز» 2 · «فود کورت تهران» 2 · «تاریخچه فست فود» 2 · «اجاره مغازه فست فود در تهران» 3 · «دانشگاه تهران» 4.

**Activity seeds (do it yourself)**
- 1: the activity narrowed, how to do it, the machine or tool for it, its cost.
- 2: one step broader, close rival activities.
- 3: different activities in the field.
- Seed «چاپ لیوان»: «چاپ روی لیوان شیشه ای» 1 · «دستگاه چاپ لیوان» 1 · «انواع چاپ» 2 · «قیمت چاپ بنر» 3 · «کاردستی با لیوان کاغذی» 4.

**Animals and things you keep**
- 1: the breed or kind narrowed, buying it, keeping, feeding, training, lifespan, a vet for it.
- 2: its cage, food and gear, another breed or kind of the same animal.
- 3: other animals and their needs.
- Seed «مرغ عشق»: «مرغ عشق ابلق» 1 · «عمر مرغ عشق» 1 · «مرغ قناری» 2.

**Investment and money seeds**
- 1: the asset narrowed (weight, karat, issuer), buying it and its price, buy-or-not questions and comparisons.
- 2: rival assets of the same kind (another metal, coin or bond), its market price and news, converting it, an exchange or dealer that sells it.
- 3: other things in the field (jewelry for a gold bar), the whole field.
- Seed «شمش طلا»: «شمش بهتره یا سکه» 1 · «قیمت شمش نقره» 2 · «انس طلا» 2 · «دستبند طلا ظریف دخترانه» 3.

## 8. Fine lines

### 8.1 Narrower is 1, broader is 2

The two directions are not equal. Adding detail keeps the searcher's need; dropping detail widens it.
- Seed «خرید تلویزیون شیائومی»: «خرید تلویزیون شیائومی ۴۳ اینچ» 1 · «خرید تلویزیون» 2 · «کالای دیجیتال» 3.
- One step means dropping one qualifier, or moving up to the parent category. Two or more steps, up to the whole field, is 3.
- «انواع» of the seed itself is 1 («انواع سرخ کن بدون روغن» for «سرخ کن بدون روغن»). «انواع» of its parent is one step broader, 2 («انواع تور» for «تور قشم»).

### 8.2 Brands and models

| Seed | Keyword | Level |
|---|---|---|
| No brand («خرید تلویزیون») | Adds a brand or model («تلویزیون سامسونگ») | 1 |
| Names a brand («خرید تلویزیون شیائومی») | Drops the brand («خرید تلویزیون») | 2 |
| Names a brand | The brand alone («شیائومی») | 2 |
| Names a brand | A rival brand of the same product («تلویزیون سامسونگ») | 2 |
| Names a brand | The same brand's other product («گوشی شیائومی») | 3 |
| No brand | A brand alone («سامسونگ») | 3 |
| Any | Another brand's other product («گوشی سامسونگ» for «خرید تلویزیون شیائومی») | 3 |
| Any | The brand's name in another need («تنظیم ساعت گوشی هواوی» for «ساعت هواوی») | 4 |

A model code is the model of whatever product it belongs to («a52» is a Samsung phone): work out the product, then use the table. If you can't tell what a code is, and the keyword puts it next to the seed's own words, read it as a model of the seed's product.

### 8.3 Places

First decide which role the place plays in the seed.

**The place only narrows the seed** (local services, venues, lawyers, clinics):
- the seed with a smaller area → 1 («فست فود شرق تهران»)
- the seed without its place → 2
- the same need in another place → 2 («فست فود شیراز»)
- a similar kind of place in the same city → 2 («فود کورت تهران»)
- anything else that only shares the place → 4 («دانشگاه تهران»)

**The place is the point** (trips, tours, stays, moving or studying abroad):
- what the seed itself includes there → 1 («جاهای دیدنی قشم» for «تور قشم»)
- another kind of stay or tour in the same place → 2 («اجاره ویلا در مشهد» for «اجاره سوئیت در مشهد»)
- the destination alone → 2 («قشم» for «تور قشم»)
- the same trip or plan for another place → 2 («اجاره سوئیت تهران» for «اجاره سوئیت در مشهد»)
- getting there, and other needs of the same trip → 3 («بلیط چارتر تهران مشهد» for «اجاره سوئیت در مشهد»)
- things there that serve no trip or plan → 4 («اقتصاد آلمان» for «هزینه زندگی آلمان»)

### 8.4 Another need on the same thing

Ask whose need it is and at what stage.

| The keyword is about | Product seed | Service, condition, topic or animal seed |
|---|---|---|
| Its price, specs, quality, what it is | 1 | 1 |
| Preparation, aftercare, results, side effects, treatment, specialists | — | 1 |
| Keeping, feeding, training (animals) | — | 1 |
| Installing, setting up, using, converting, diagnosing a fault | 2 | 2 |
| Training to provide it, careers in it | 2 | 2 |
| Repair, recharging or maintenance by someone else; a separate cost | 3 | 3 |

- «علت امپر کشیدن پمپ شناور» (why a submersible pump draws too much current) is 2 for «قیمت پمپ شناور»: the owner diagnosing a fault.
- «تعمیر اسپیکر» is 3 for «اسپیکر»: a repair service, a later need served by someone else.
- «مراقبت بعد از کراتین مو» is 1 for «کراتین مو»: aftercare is part of getting the service.
- «هزینه مهاجرت به آلمان» is 3 for «هزینه زندگی آلمان»: a separate cost around the plan.

### 8.5 Rivals: close (2) or distant (3)

- **Close rival (2):** an interchangeable version of the same kind of thing, where only the brand, model, type, material, breed, vehicle or target changes. «تلویزیون سامسونگ» for «خرید تلویزیون شیائومی», «قیمت شمش نقره» for «شمش طلا», «مرغ قناری» for «مرغ عشق», «دستکش کاراته» for «خرید دستکش بوکس», «اجاره ویلا در مشهد» for «اجاره سوئیت در مشهد», «ترک قلیان» for «ترک سیگار», «قیمت تخلیه چاه» for «لوله بازکنی».
- **For conditions,** a related condition people check against the seed is a close rival: «سردرد تنشی چیست» for «درمان میگرن» is 2. Another condition in the same area of medicine is 3: «تشنج میوکلونیک».
- **Distant rival (3):** a different product, service or procedure in the same category that works differently or does another job. «بوتاکس مو» for «کراتین مو», «قیمت چاپ بنر» for «چاپ لیوان».

### 8.6 Complements (2) and neighbors (3)

- **Complement (2):** a product used together with the seed, or the setup it belongs to («سیستم صوتی خانگی» for «اسپیکر»); a place to learn what the seed's field needs («آموزشگاه کامپیوتر» for «مهندسی کامپیوتر»).
- **Neighbor (3):** another product or service the same customer might buy separately («دستبند طلا ظریف دخترانه» for «شمش طلا», «سالن میکاپ عروس» for «تالار عروسی»).
- A service from someone else is 3 even when it is closely tied to the seed, like drilling the well a pump goes into («هزینه حفر چاه آب» for «قیمت پمپ شناور»). Installing is the one exception: 2.

### 8.7 The business side

| The keyword is about | Level |
|---|---|
| The seed's item bought wholesale | 1 |
| A store, marketplace, dealer, exchange or agency that sells it | 2 |
| A factory, production line or machine to manufacture it | 3 |
| Opening or renting a shop to sell it | 3 |
| A company that only shares a word | 4 |

When the seed is itself an activity, the machine that does that activity is its tool: «دستگاه چاپ لیوان» is 1 for «چاپ لیوان».

### 8.8 Jobs and learning

| The keyword is about | Level |
|---|---|
| Learning the seed, when the seed is a subject or skill to learn | 1 |
| Training to provide the seed's service | 2 |
| Careers, hiring or pay in the seed's own field or trade | 2 |
| A job at a company that only shares a word | 4 |
| A job in another field with no shared word | 5 |
| A wording that can mean the customer's need («نیازمند لوله کش») | Read it as the need: usually 1 |

### 8.9 Opposite needs

A keyword that works against the seed's need is not found, even when it is on the same subject: «قیمت سیگار عمده» (wholesale cigarette prices) for «ترک سیگار» (quitting smoking) is 4, because it shares «سیگار».

### 8.10 Shared words

- A real relation beats shared words: a keyword at levels 1–3 stays there whatever it shares.
- Shared words beat nothing: a keyword with no relation is 4 when it shares something visible with the seed, and 5 only when it shares nothing.

## 9. Keyword forms

- **Spelling:** typos, missing or extra spaces, half-spaces, Arabic «ي» and «ك», colloquial spellings: grade by meaning («لپتاپ» is «لپ تاپ», «ویزه» is «ویزا»). If the meaning can't be recovered → 6.
- **Script and language:** Latin script, Finglish and English translations count by meaning («asus laptop» for «لپ تاپ ایسوس» → 1). So do Arabic and other languages when the meaning is clear.
- **Numbers, sizes, years and model codes** are qualifiers: «6 اینچ», «۱۴۰۲», «a52».
- **Questions** («… چیست», «آیا …», «چرا …», «… بهتره یا …»): grade the subject and need; the question form changes nothing.
- **Long keywords:** grade the keyword's main need. Extra words that only qualify it (a city, a brand, a year) narrow it.
- **Two subjects in one keyword** («ماشین لباسشویی و ظرفشویی سامسونگ»): if one of them is the seed's thing, grade it as being about that thing.
- **The seed itself,** in any spelling or word order: 1.
- **Unknown words** (a brand, model, place, name, slang or technical term you don't recognize or aren't sure of, in the seed or a keyword): search the web for what it means before grading. Look up only the meaning, never the keyword's rankings, sites or search volume. A word with several meanings counts each common one (section 3). If the search doesn't settle it, judge from the rest of the keyword, and if you still can't tell, give your best reading plus a second choice.
- **Sensitive subjects** (sexual health, drugs, tobacco, religion, politics): grade the relation like any other. Never move a level for taste.
- **Ignore** search volume, commercial value, how well-formed the keyword is and whether it would make a good page.

## 10. Worked seeds

Each table is one seed with keywords across the scale.

**«قیمت 206»** (the price of the Peugeot 206 car)

| Keyword | Level | Why |
|---|---|---|
| «قیمت 206 صفر» | 1 | The price of a new one: narrowed |
| «قیمت 207» | 2 | Another model's price: a close rival |
| «نرخ ثالث 1401» | 3 | Car insurance rates: another need of a car owner |
| «قیمت پر قو» | 4 | Down feathers: shares only «قیمت» |
| «صفر تا صد خیاطی» | 5 | Learning to sew: nothing in common |
| «قیمت» | 6 | Too generic |

**«هاست»** (web hosting)

| Keyword | Level | Why |
|---|---|---|
| «هاستینگ ارزان» | 1 | Cheap hosting |
| «انتقال سایت به هاست» | 2 | Moving a site onto it: a side task |
| «طراحی سایت تهران وب داران» | 3 | Web design: a neighbor service |
| «هاستل» | 4 | A hostel: a similar spelling |
| «چک لیست کمپینگ» | 5 | A camping checklist |
| «آنلاین» | 6 | Too generic |

**«گچبری پیش ساخته»** (prefab plaster molding)

| Keyword | Level | Why |
|---|---|---|
| «مدلهای گچبری پیش ساخته» | 1 | Its designs |
| «نصاب گچبری پیش ساخته» | 2 | Installing it |
| «گچ کاری ساده» | 3 | Wall plastering: a neighbor trade |
| «گچ خیاطی» | 4 | Tailor's chalk: «گچ» in another sense |
| «دوبل برگر چیست» | 5 | A double burger |
| «گگ» | 6 | Broken text |

**«خرید تلویزیون شیائومی»** (buy a Xiaomi TV)

| Keyword | Level | Why |
|---|---|---|
| «خرید تلویزیون شیائومی ۴۳ اینچ» | 1 | A size: narrowed |
| «کیفیت تلویزیون های شیائومی» | 1 | Information for the purchase |
| «خرید تلویزیون» | 2 | One step broader |
| «تلویزیون سامسونگ» | 2 | A rival brand |
| «کنترل تلویزیون شیائومی» | 2 | A part made for it |
| «گوشی شیائومی» | 3 | The same brand's other product |
| «کالای دیجیتال» | 3 | The whole field |
| «گوشی شیائومی به تلویزیون» | 4 | Connecting a phone to a TV: shares words only |
| «قیمت» | 6 | Too generic |

**«قیمت پمپ شناور»** (submersible pump prices)

| Keyword | Level | Why |
|---|---|---|
| «قیمت پمپ شناور 6 اینچ» | 1 | A size: narrowed |
| «علت امپر کشیدن پمپ شناور» | 2 | Diagnosing a fault |
| «نمایندگی پمپیران» | 2 | A dealer that sells it |
| «هزینه حفر چاه آب» | 3 | Well drilling: a separate service |
| «استخدام اطلس پمپ سپاهان» | 4 | Hiring at a pump company: shares «پمپ» |

**«تالار عروسی»** (wedding hall)

| Keyword | Level | Why |
|---|---|---|
| «تالار عروسی غرب تهران» | 1 | Narrowed to an area |
| «جشن عروسی ایرانی» | 1 | The event the hall is for |
| «قیمت منو تالار عروسی» | 2 | The hall's catering menu: an add-on |
| «سالن میکاپ عروس» | 3 | Bridal makeup: another service for the same day |

**«وکیل ملکی»** (property lawyer)

| Keyword | Level | Why |
|---|---|---|
| «وکیل ملکی شیراز» | 1 | Narrowed to a city |
| «انواع وکیل» | 2 | One step broader |
| «محاسبه حق کمیسیون املاک» | 3 | Real-estate agent fees: a neighbor in the field |
| «قرارداد وکیل و موکل» | 3 | Lawyer contracts in general: a neighbor in the field |

**«لوله بازکنی»** (drain unclogging)

| Keyword | Level | Why |
|---|---|---|
| «قیمت لوله بازکنی» | 1 | Its price: reworded |
| «نیازمند لوله کش» | 1 | "I need a plumber": the same need |
| «قیمت تخلیه چاه» | 2 | Emptying a cesspit: a close rival service |
| «لوله گالوانیزه» | 4 | Galvanized pipe: shares «لوله» |

**«باتری خودرو»** (car battery)

| Keyword | Level | Why |
|---|---|---|
| «باتری پراید» | 1 | Narrowed to a car model |
| «هزینه شارژ باتری ماشین» | 3 | Recharging: a paid service |
| «کارخانه تولید باتری خودرو» | 3 | A factory |

**«سرخ کن بدون روغن»** (air fryer)

| Keyword | Level | Why |
|---|---|---|
| «سرخ کن بدون روغن شیائومی» | 1 | Narrowed to a brand |
| «توری سرخ کن» | 2 | A part made for it |
| «ظرف روغن مایع» | 4 | An oil container: shares «روغن» |

**«مهندسی کامپیوتر»** (computer engineering, the field of study)

| Keyword | Level | Why |
|---|---|---|
| «بازار کار مهندسی کامپیوتر» | 1 | The job market it leads to |
| «آموزشگاه کامپیوتر» | 2 | A computer school: a complement |
| «استخدام مهندس کامپیوتر» | 2 | Careers in the field |

**«اجاره سوئیت در مشهد»** (renting a suite in Mashhad)

| Keyword | Level | Why |
|---|---|---|
| «اجاره ویلا در مشهد» | 2 | Another kind of stay in the same place |
| «اجاره سوئیت تهران» | 2 | The same stay in another city |
| «بلیط چارتر تهران مشهد» | 3 | Getting there |

**«خرید دستکش بوکس»** (buy boxing gloves): «دستکش کاراته» 2 (a close rival).

The other seeds used above («اسپیکر», «کراتین مو», «درمان میگرن», «ترک سیگار», «تور قشم», «هزینه زندگی آلمان», «فست فود تهران», «چاپ لیوان», «مرغ عشق», «شمش طلا») have their worked lists in section 7.

## 11. Contrast pairs

Close pairs that land on different levels, and what decides them.

| Seed | Keyword A | Keyword B | What decides it |
|---|---|---|---|
| «اسپیکر» | «پایه اسپیکر خانگی» 2 | «تعمیر اسپیکر» 3 | A part made for it vs a repair service |
| «خرید تلویزیون شیائومی» | «تلویزیون سامسونگ» 2 | «گوشی شیائومی» 3 | A rival of the same product vs the same brand's other product |
| «خرید تلویزیون شیائومی» | «گوشی شیائومی» 3 | «گوشی شیائومی به تلویزیون» 4 | A real neighbor vs a different need built from the same words |
| «کراتین مو» | «مراقبت بعد از کراتین مو» 1 | «بوتاکس مو» 3 | Part of getting the service vs a different procedure |
| «کراتین مو» | «کراتین مو مشهد» 1 | «کراتین بدنسازی» 4 | The same service vs a word spelled the same |
| «درمان میگرن» | «سردرد تنشی چیست» 2 | «تشنج میوکلونیک» 3 | A related condition people check against it vs another condition |
| «تور قشم» | «جاهای دیدنی قشم» 1 | «بلیط اتوبوس به قشم» 3 | Part of the tour vs getting there |
| «اجاره سوئیت در مشهد» | «اجاره ویلا در مشهد» 2 | «بلیط چارتر تهران مشهد» 3 | Another stay vs getting there |
| «فست فود تهران» | «فود کورت تهران» 2 | «دانشگاه تهران» 4 | A similar place in the same city vs something else in the city |
| «ترک سیگار» | «ترک قلیان» 2 | «قیمت سیگار عمده» 4 | Quitting another tobacco vs working against the need |
| «وکیل ملکی» | «انواع وکیل» 2 | «قرارداد وکیل و موکل» 3 | One step broader vs another thing in the legal field |
| «قیمت پمپ شناور» | «نمایندگی پمپیران» 2 | «استخدام اطلس پمپ سپاهان» 4 | A dealer that sells it vs a job that shares a word |
| «مهندسی کامپیوتر» | «بازار کار مهندسی کامپیوتر» 1 | «استخدام مهندس کامپیوتر» 2 | The outcome you weigh when choosing it vs a later career step |
| «خرید تلویزیون شیائومی» | «خرید تلویزیون» 2 | «کالای دیجیتال» 3 | One step broader vs the whole field |

## 12. Mistakes to avoid

- **Giving 1 to everything on the subject.** Broader keywords, rivals, accessories, add-ons and side tasks are 2; neighbors and paid services are 3.
- **Giving 4 to a related keyword** because it shares a word. If it has a real relation, it is 1, 2 or 3.
- **Giving 5 to a keyword that shares a word with the seed.** With no relation, it is 4.
- **Treating a shared city as a relation.** Outside trips and moves abroad, sharing only the place is 4.
- **Confusing no topic with broader.** «قیمت» alone is 6, not one step broader of «قیمت پمپ شناور»; «پمپ» alone has a topic and is 2.
- **Lowering a keyword** for its spelling, English words, brand names or question form.
- **Raising a keyword** because it is popular, commercial or looks like a good keyword.
- **Letting the list move your scale.** Grade each keyword against the seed alone, not against the other keywords.
- **Rewarding opposite needs.** A keyword that works against the seed's need is not found.
- **Splitting the difference.** When torn, give a first and a second choice instead of a level in between that fits neither.

## 13. Consistency

- The same seed and keyword always get the same level.
- The same relation gets the same level across seeds: a rival brand of the same product is 2 for every product seed.
- There are no quotas. A seed can have twenty 1s or none.
- Each batch is graded on its own. Don't rely on what you graded before; this guide is the only reference.
- For a case this guide doesn't cover, grade it like the closest rule or example and add a short note.

## 14. Output format

Write one line per seed: its id, a colon, then every keyword's number and level, in list order.

```
R0001: 1=1 2=4 3=2/3 4=6 5=1 6=3 (getting there) 7=5
```

- `<number>=<level>`: the keyword's number in the batch, then its level, 1–6.
- `<number>=<first>/<second>`: torn between two levels; the first is your choice, the second the other one that fits. The two must differ.
- `(note)`: a short note right after an entry, only for a case this guide doesn't cover.
- Grade every keyword in the list; never skip one or grade one twice.

## 15. Before you submit

- Every keyword has exactly one entry.
- Level 6 was checked first, and nothing with a topic of its own got it.
- Every 4 shares something visible with the seed; every 5 shares nothing.
- Every 1 is the same thing for the same need; nothing broader got 1.
- Rivals are 2 or 3, never 1.
- Repairs and separate paid services are 3; installing is 2.
- Second choices are rare: as a rule of thumb, fewer than one keyword in ten.

---

## Appendix

### A. Fields

Use these to judge "the same field" (level 3) and "the whole field". A field is about the size of one of these areas:

- **Economy:** forex, investment funds, the stock exchange, cryptocurrency, trade, banking and insurance
- **Marketing and advertising:** digital marketing, websites and SEO, offline advertising, public relations
- **Technology:** communication equipment, online apps, servers and hosting, social media, computer hardware, software tutorials
- **Beauty and personal care:** perfume, skin and hair care, cosmetics
- **Education:** fields of study, schools and universities, entrance exam (Konkur) classes and books, books and reading, language learning
- **Law:** business, family and commercial law, lawyers, legal know-how
- **Pets:** dogs and cats, birds, other pets, pet diseases
- **Home and kitchen:** housekeeping, kitchenware, flowers and plants, household items
- **Services:** transport and moving, appliance repair, financial services, cleaning
- **Automotive:** maintenance and repair, car costs, buying and selling cars
- **Events:** celebrations, religious occasions, festivals and prize draws
- **Entertainment:** recreation centers, movies and series, theater and cinema, games and toys, video games, podcasts, music, learning skills
- **Industry:** agriculture, industrial supplies, machinery
- **Construction and buildings:** building security, maintenance, architecture and interior design, real-estate law, buying and renting property, building equipment and components
- **Fashion:** jewelry, clothing
- **Jobs and careers:** job training, hiring
- **Immigration:** immigration routes, document translation, residency, study abroad
- **Sensitive topics:** tobacco, marital relations
- **Sports:** sports equipment, sports news
- **Health and medicine:** diseases and treatments, counseling and psychology, diet, dentistry, skin and hair treatment, medicines and medical equipment, surgery, cosmetic surgery, doctors, health tips
- **Electronics:** smartwatches, mobile phones, consoles, computers and peripherals, digital gadgets, accessories
- **Travel and tourism:** flights, destinations, pilgrimage trips, tickets, attractions, hotels and stays

### B. Names you should recognize

Keywords often narrow a seed with Iranian names. Recognize them as qualifiers, not as other subjects.

- **Cars:** پراید, پژو ۲۰۶, ۴۰۵ and پارس, سمند, دنا, رانا, تیبا, ساینا, کوییک, شاهین, ال ۹۰, ام وی ام, جک, لیفان, هایما, چری
- **Appliance and electronics brands:** پارس خزر, اسنوا, امرسان, جی پلاس, دوو, ال جی, سامسونگ, بوش, تفال, فیلیپس, شیائومی, هواوی
- **Stores and marketplaces:** دیجی کالا, ترب, باسلام, دیوار, شیپور
- **Crypto exchanges and banks:** نوبیتکس, والکس, رمزینکس, بایننس; بانک ملی, ملت, سپه
- **Mobile operators:** همراه اول, ایرانسل, رایتل
- **Places:** Tehran and its districts («غرب تهران», «سعادت آباد»), مشهد, اصفهان, شیراز, تبریز, کرج, قم, the islands کیش and قشم, and «شمال» (the Caspian provinces, a common trip destination)
- **Units:** «گرمی» (grams, for gold), «عیار» (karat), «اینچ» (inches), «نفره» (people, for sets and tables), «کیلویی» (kilograms, for washing machines)
