// to do translating melon_counting.py code into JS

melonsToAdd = ['Ogen', 'Horned Melon', 'Watermelon', 'Casaba', 'Sharlyn', 'Xigua', 'Ogen', 'Christmas', 'Christmas',
'Christmas', 'Christmas', 'Watermelon', 'Sharlyn', 'Xigua','Cantaloupe', 
'Christmas', 'Watermelon', 'Christmas','Sharlyn', 'Christmas', 'Cantaloupe', 'Casaba', 'Cantaloupe',
'Santa Claus', 'Horned Melon', 'Watermelon', 'Ogen',
'Horned Melon', 'Cantaloupe', 'Xigua', 'Horned Melon', 'Sharlyn',
'Horned Melon', 'Sharlyn', 'Cantaloupe', 'Christmas',
'Horned Melon', 'Horned Melon', 'Horned Melon', 'Xigua', 'Xigua',
'Watermelon', 'Cantaloupe', 'Casaba', 'Cantaloupe', 'Casaba',
'Watermelon', 'Santa Claus', 'Casaba']


const countMelons = (melonList) => {
    melonCounts = {}

    for (let melon of melonList) {
        if (Object.keys(melonCounts).includes(melon)) {
            melonCounts[melon] = melonCounts[melon] + 1
        } else {
            melonCounts[melon] = 1
        }
    }
    console.log(melonCounts)
}

countMelons(melonsToAdd)
