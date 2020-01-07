# coding=utf-8

from __future__ import unicode_literals
from .. import Provider as CompanyProvider


class Provider(CompanyProvider):

    formats = (
        '{{first_name}} և {{first_name}} {{company_suffix}}',
        '{{last_name} {{company_suffix}}',
        '{{last_name}} և {{last_name}} {{company_suffix}}'
        '{{last_name}}, {{last_name}} և {{last_name}} {{company_suffix}}',
    )

    company_suffixes = ('ՍՊԸ', 'ՀՁ', 'ՓԲԸ', 'ԲԲԸ', 'Գրուպ', 'Հոլդինգ')

    catch_phrase_words = (
        ('առաջավոր',
         'բարելավված',
         'ավտոմատացված',
         'հավասարակշռված',
         'կենտրոնացված',
         'համատեղելի',
         'կարգավորելի',
         'անհատականացված',
         'ապակենտրոնացված',
         'թվայնացված',
         'տարածված',
         'փոքրացված',
         'ընդլայնված',
         'էրգոնիկ',
         'բացառիկ',
         'երկարացված',
         'լիովին կոնֆիգուրացվող',
         'ֆունկցիոնալ հիմունքներով',
         'հիմնական',
         'հորիզոնական',
         'իրականացված',
         'նորարական',
         'ինտեգրված',
         'ինտուիտիվ',
         'պարտադիր',
         'բազմուղի',
         'բազմաշերտ',
         'ցանցային',
         'բաց կոդով',
         'օպերատիվ',
         'օպտիմալացված',
         'օրգանական',
         'կազմակերպված',
         'կայուն',
         'կենսունակ',
         'ավարտված',
         'բևեռացված',
         'կանխարգելող',
         'ակտիվ',
         'ծրագրավորելի',
         'առաջադիմական',
         'որակով',
         'ռեակտիվ',
         'իրականացված',
         'նվազեցված',
         'դիմացկուն',
         'անխափան',
         'ապահով',
         'համատեղելի',
         'հեշտացված',
         'փոխարկելի',
         'սինխրոնիզացված',
         'ունիվերսալ',
         'ճկուն',
         'վիրտուալ'),
        ('3-րդ սերնդի',
         '4-րդ սերնդի',
         '5-րդ սերնդի',
         '6-րդ սերնդի',
         'ասիմետրիկ',
         'ասինխրոն',
         'թողունակությունը վերահսկվող',
         'երկկողմանի',
         'հստակ մտածող',
         'համաձայնեցված',
         'բաղադրյալ',
         'դիդակտիկ',
         'ուղղորդիչ',
         'դիսկրետ',
         'բացահայտ',
         'գլոբալ',
         'բարձր մակարդակի',
         'ամբողջական',
         'միատարր',
         'հիբրիդ',
         'ազդեցիկ',
         'ինտերակտիվ',
         'միջանկյալ',
         'առաջատար',
         'տեղային',
         'լոգիստիկ',
         'սիստեմատիկ',
         'մոդուլային',
         'չեզոք',
         'հաջորդ սերնդի',
         'օբյեկտի վրա հիմնված',
         'օպտիմալ',
         'արմատական',
         'փոխադարձ',
         'ռեգիոնալ',
         'երկրորդական',
         'կայուն',
         'ստատիկ',
         'համակարգված',
         'համակարգային',
         'շոշափելի',
         'երրորդական',
         'անցումային',
         'միատեսակ',
         'լավ մոդուլացված',
         'առանց թերությունների'),
        ('կարողություն',
         'մուտք',
         'ադապտեր',
         'ալգորիթմ',
         'միություն',
         'վերլուծիչ',
         'ծրագրային ապահովում',
         'մոտեցում',
         'արխիվ',
         'արհեստական բանականություն',
         'վերաբերմունք',
         'ընդունակություն',
         'կարողություն',
         'մարտահրավեր',
         'գործակցություն',
         'բարդություն',
         'գաղափար',
         'համախմբվածություն',
         'տվյալների բազա',
         'տվյալների պահեստ',
         'սահմանում',
         'իմացություն',
         'կոդավորում',
         'գաղտնագրում',
         'կանխատեսում',
         'հենքային ծրագիր',
         'ֆունկցիա',
         'գործառույթ',
         'գրաֆիկական ինտերֆեյս',
         'սարքային ապահովում',
         'հիերարխիա',
         'հանգույց',
         'ենթակառուցվածք',
         'նախաձեռնություն',
         'ծրագրի ներդրում',
         'հրահանգների հավաքածու',
         'ինտերֆեյս',
         'ինտրանետ',
         'գիտելիքների բազա',
         'տեղական ցանց',
         'մատրիցա',
         'մեթոդաբանություն',
         'միջանկյալ շերտ',
         'միգրացիա',
         'մոդել',
         'կարգավորիչ',
         'մոնիտորինգ',
         'բաց համակարգ',
         'պարադիգմ',
         'պորտալ',
         'գնային կառուցվածք',
         'արդյունավետություն',
         'նախագիծ',
         'ապահովված գիծ',
         'ծրագրային ապահովում',
         'լուծում',
         'ստանդարտացում',
         'ստրատեգիա',
         'կառուցվածք',
         'օպերատիվ խումբ',
         'արտադրողականություն',
         'ժամանակացույց',
         'գործիք',
         'օգտագործում',
         'կայք',
         'աշխատուժ'))

    bsWords = (
        ('իրականացնել',
         'օգտագործել',
         'ինտեգրել',
         'ռացիոնալացնել',
         'օպտիմալացնել',
         'փոխակերպել',
         'ընդգրկել',
         'ակտիվացնել',
         'կազմակերպել',
         'նախագծել',
         'խթանել',
         'ձևափոխել',
         'արտոնել',
         'դրամայնացնել',
         'հեշտացնել',
         'վերցնել',
         'աճեցնել',
         'սինթեզել',
         'առաքել',
         'զբաղվել',
         'առավելագույնի հասցնել',
         'արագացնել',
         'միջնորդել',
         'պատկերացնել',
         'վերափոխել',
         'ընդլայնել',
         'նախաձեռնել',
         'հեղափոխականացնել',
         'առաջացնել',
         'օգտագործել',
         'զարգացնել',
         'արտադրանքի վերածել'),
        ('ուղղահայաց',
         'ակտիվ',
         'դիմացկուն',
         'հեղափոխական',
         'առաջատար',
         'նորարարական',
         'ինտուիտիվ',
         'ռազմավարական',
         'էլեկտրոնային',
         'գլոբալ',
         'վիրտուալ',
         'դինամիկ',
         'գրավիչ',
         'ինտերակտիվ',
         'արդյունավետ',
         'ընդարձակելի',
         'պատրաստի',
         'ինտեգրված',
         'ազդեցիկ',
         'անլար',
         'թափանցիկ',
         'հաջորդ սերնդի',
         'ժամանակակից',
         'հարմարեցված',
         'համատարած',
         'ազդեցիկ',
         'ամբողջական',
         'հարուստ',
         'անվճար'),
        ('պարադիգմներ',
         'շուկաներ',
         'ենթակառուցվածքներ',
         'պլատֆորմներ',
         'նախաձեռնություններ',
         'ուղիներ',
         'համայնքներ',
         'լուծումներ',
         'պորտալներ',
         'տեխնոլոգիաներ',
         'հարաբերություններ',
         'կառուցվածքներ',
         'ինտերֆեյսներ',
         'շուկաներ',
         'համակարգեր',
         'մոդելներ',
         'օգտագործողներ',
         'սխեմաներ',
         'ցանցեր',
         'ծրագրեր',
         'չափանիշներ',
         'բիզնես',
         'գործառույթներ',
         'փորձառություններ',
         'մեթոդաբանություններ'))
