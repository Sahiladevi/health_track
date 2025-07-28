# Analyzing the Impact of Lifestyle, Socioeconomic Status, and Healthcare Access on Chronic Health Conditions Among U.S. Adults

---

## Introduction

Chronic health conditions such as obesity, diabetes, high blood pressure, high cholesterol and heart diseases continue to rise among U.S. adults. While medical advances have helped manage these conditions, less attention has been paid to the root causes like poor diet, physical inactivity, inadequate sleep, and limited access to healthcare. These lifestyle and social factors are deeply interconnected, and they don’t affect everyone equally. People from lower-income backgrounds or certain racial and ethnic groups often face greater barriers to staying healthy.

Despite the availability of large national health surveys, we still lack a clear, up-to-date understanding of how these everyday factors combine to shape health outcomes. This project aims to fill that gap using recent NHANES and USDA data to explore how lifestyle and social variables are tied to health—offering insights that can inform public health efforts and personalized health advice.

---

## Goal 1: How Lifestyle and Life Circumstances Shape Our Health

I wanted to explore how the way we live our habits, routines, and even the resources we have access to, can shape our health over time. So I looked at things like what people eat, how much they sleep or move around, and their life circumstances, like income, education, and health insurance.

My goal was to see how all of that connects to chronic health problems in adults across the U.S., things like obesity, diabetes, high blood pressure, and heart disease. It’s not just about one factor, but how everything adds up and affects people differently based on their background and lifestyle.

By doing this, I hoped to better understand what puts certain groups more at risk and what changes might actually help people live healthier lives.

---

### Objective 1.1 – What Does the Data Say About Our Health and Lifestyle?

In this part of my project, I wanted to get a basic understanding of how people in the U.S. are doing when it comes to diet, physical activity, sleep, insurance, education, and income. I used data from NHANES 2021–2023, which collects detailed health info from people across the country.

I looked at both:

- Unweighted data – what people actually said in the survey.

- Weighted data – adjusted numbers that show what this would look like across the whole U.S. adult population.

The weighted results give a better national picture, so I mainly focused on those, but I included both in my analysis.

**What I Found**

#### Diet Quality

82.4% of U.S. adults have poor diet quality.

Even in the raw (unweighted) data, about 80% eat poorly.

[Plot: Diet Score Distribution]
Most people are not eating healthy diets. The chart shows a heavy tilt toward low scores.

#### Physical Activity

Over half (52%) of adults are low active.

Only about 1 in 4 are getting enough exercise.

[Plot: Weekly Activity & Activity Levels]
The chart clearly shows that many people aren't moving enough.

#### Sleep Duration

7.7% sleep less than 7 hours.

79.1% sleep between 7–9 hours (healthy range).

13.2% sleep more than 9 hours.

[Plot: Sleep Duration Histogram]
Most are sleeping fine, but some get too little or too much sleep.

#### Health Insurance

91.2% of adults have health insurance.

About 9% do not.

[Plot: Insurance Coverage Pie Chart]
Even though most people are covered, millions still don’t have insurance.

#### Education

9.5% didn’t finish high school.

About 36% have a college degree or higher.

[Plot: Education Levels]
Many people started college but didn’t finish. A smaller group finished college or beyond.

#### Income (Poverty Ratio - PIR)

The average poverty ratio is 3.06 (weighted).

The unweighted average is slightly lower, at 2.91.

[Plot: PIR Distribution]
A lot of people are living near or below the poverty line.

#### Race & Ethnicity
61% are Non-Hispanic White.

Followed by Black (10.5%), Hispanic, Asian, and Multiracial groups.

[Plot: Race/Ethnicity Chart]
The data shows that the U.S. is very diverse, which matters when making health programs that work for everyone.

**What Can Be Done?**

Here are some real-life steps we can take based on the data:

***Help People Eat Healthier***
Most adults have poor diets. Things like nutrition classes, healthy food access, and cooking programs can help.

***Support More Physical Activity***
Many people aren’t active. We need more parks, free classes, and safe places to move.

***Raise Awareness About Sleep***
Some people aren’t getting the right amount of sleep. Teaching about good sleep habits can help.

***Close the Insurance Gap***
9% without insurance is still a lot. More outreach in rural or low-income areas could help people get covered.

***Make Health Info Easy to Understand***
Since the population is so diverse, health messages should be in plain language, offered in different languages, and made for all education levels.

**Final Thoughts**
This first step gave me a good overview of how people in the U.S. are doing. Even though some of the numbers look worrying like poor diet and low activity,it also shows where we can step in and help.

The charts made it easier to see the problems. And the numbers (both weighted and unweighted) told the same story:
- There’s a lot of room to improve health and reduce gaps, especially with small, targeted changes.

---

### Objective 1.2 – What Influences Our Health?

Sometimes, health outcomes like BMI, blood pressure, or cholesterol aren’t just about one habit—but a mix of lifestyle, income, education, age, and more. So here, I used regression models to ask: what really shapes our health? Here’s what I found:

#### 1. What Raises or Lowers BMI?

To understand what affects people’s weight (BMI), I looked at their activity, diet, sleep, education, income, and more.

**What I found:**

People who are less active tend to have higher BMI.

Getting more sleep and eating a healthier diet are linked to slightly lower BMI.

College graduates had lower BMI compared to those with less education.

Non-Hispanic Asian adults had much lower BMI than all other groups.

Age and income didn’t seem to make a big difference here.

***Plot: Lifestyle + Demographics → BMI (Regression Coefficient Plot: Factors Predicting BMI)***

The chart shows which traits push BMI higher or lower. It's a quick way to see what really matters.

#### 2. What Affects Blood Pressure the Most?

Here I looked at two parts of blood pressure: the top number (systolic) and bottom number (diastolic), and how they relate to lifestyle and background.

**What I found:**

Systolic BP (top number) goes up with age, and is higher in men and Non-Hispanic Black adults.

Diet quality helped bring it down a little.

Diastolic BP (bottom number) also rose with age and lower physical activity.

People who slept more had slightly lower diastolic BP.

So blood pressure is heavily influenced by age, gender, activity, and race.

***Plot: Lifestyle + Demographics → Blood Pressure (Coefficient Plots for Systolic & Diastolic BP)***

The charts show how each factor pushes BP up or down—making it easy to spot key contributors.

#### 3. What Drives Up Cholesterol?

Next, I looked at total cholesterol levels, and whether things like diet, activity, and income had any clear effect.

**What I found:**

Surprisingly, men had lower cholesterol than women.

Low-income people had slightly higher cholesterol.

Being inactive may raise cholesterol a bit, but results weren’t very strong.

Overall, we didn’t find strong patterns here—cholesterol may depend more on genetics, medication, or other factors not measured.

***Plot: Lifestyle + Demographics → Cholesterol (Coefficient Plot for Total Cholesterol)***

The graph shows small shifts in cholesterol, but no dramatic changes based on lifestyle alone.

#### 4. What Raises Blood Sugar (Glucose)?

Here I looked at fasting blood glucose—important for spotting diabetes risk.

**What I found:**

Men had higher glucose than women.

Older adults had higher glucose, too.

Better diet and being Non-Hispanic Asian were linked to lower glucose levels.

Again, activity didn’t have a huge impact here.

***Plot: Lifestyle + Demographics → Glucose (Predicted Fasting Glucose by Factors)***

The graph helps visualize how blood sugar varies across groups.

#### 5. Who’s More Likely to Have Diabetes?

This time I used a special model to predict who has diabetes based on lifestyle and background.

**What I found:**

Low activity and poor diet = higher risk.

Men had a higher chance than women.

Better education and income seemed to protect against diabetes.

Non-Hispanic White and Asian adults had the lowest risk.

Having health insurance was linked to higher diagnosis—probably because more people got tested.

***Plot: Lifestyle + Demographics → Diabetes Risk (Odds Ratios for Each Risk Factor)***

The chart shows how much each factor increases or lowers the odds of having diabetes.

#### 6. What Predicts Heart Disease?

Finally, I looked at cardiovascular disease—things like heart attacks or stroke.

**What I found:**

Poor sleep, low income, poor diet, and being inactive were big risk factors.

Older age and being male raised the risk.

People with short sleep or bad cholesterol had higher odds of heart problems.

This model combined a wide mix of health and lifestyle factors to give a fuller picture.

***Plot: Lifestyle + Clinical Factors → Heart Disease (Odds Ratio Plot for CVD Risk)***

This chart shows which factors matter most when it comes to heart health.

**What It All Means:**
Our health is shaped by many things at once—not just diet or exercise. Gender, race, age, education, income, and sleep all leave their mark. These models help us see which patterns are strongest, and who might be more at risk.

---

### Objective 1.3 – How Lifestyle and Social Factors Shape Our Health

This section explores how things like sleep, income, and education affect our weight, blood pressure, cholesterol, and diabetes risk. Each part focuses on one relationship and includes what the data showed — both in numbers and visuals.

#### 1. Does Sleeping More Help Lower Weight and Blood Pressure?
  To find out, I looked at whether people who sleep longer have healthier body weight and blood pressure.

**What I found:**

People who sleep more tend to have slightly lower BMI (a measure of weight) and better blood pressure.

For example:

- Each extra hour of sleep was linked to a small drop in BMI and both systolic and diastolic blood pressure.

- People who sleep less than 6 hours had the highest BMI.

- People who sleep 7–9 hours (normal) had the healthiest readings overall.

- Long sleepers didn’t show major changes except slightly better diastolic blood pressure.

***Plot: Sleep Hours and Categories → BMI and Blood Pressure (Scatter + Bar Plot)***

The scatter plots showed sleep hours going up while BMI and blood pressure slowly went down.
The bar plot made it clear: short sleepers stood out as having worse health, especially weight.

#### 2. Do Income and Education Affect Cholesterol Levels?

Here, I checked how people’s income and education level relate to their total cholesterol.

**What I found:**

Surprisingly, people with higher income and more education actually had slightly higher cholesterol.

That might sound strange, but it’s likely because they have more access to testing or better good cholesterol (HDL), which raises total cholesterol numbers.

College grads had the highest cholesterol on average.

People with missing education info had much lower cholesterol, which may reflect health issues or missing data.

***Plot: Income × Education → Cholesterol (Grouped Bar Plot)***
The bars clearly showed cholesterol going up with education and income. But the differences weren’t huge, and other factors probably play a role too.

#### 3. Who’s More Likely to Be Obese — and Why?

This time, I modeled the chance of being obese based on people’s income and education level.

**What I found:**

Lower income = higher obesity risk.
Less education = higher obesity risk.

It was that simple. College graduates and people with higher income were much less likely to be obese.

The biggest drop in obesity happened for college-educated groups.

Very high-income people had the lowest risk overall.

***Plot: Income × Education → Obesity (Bar Plot: Predicted Obesity Rates)***
The chart made it super clear: as income and education rise, obesity drops. You could literally see the curve flatten.

#### 4. How Do Sleep, Money, and Education Affect Diabetes Risk?

Here, I combined sleep hours, income, and education to see who’s most at risk for diabetes.

**What I found:**

Low-income, low-education groups had the highest risk of diabetes.

College-educated, higher-income people had the lowest risk.

Longer sleep hours were actually linked to a slightly higher diabetes risk, which might reflect underlying illness or fatigue.

So while more sleep helped with weight and blood pressure, it didn’t lower diabetes risk — in fact, the opposite showed up.

***Plot: Income × Education → Diabetes Risk (Bar Plot: Predicted Probability of Diabetes)***
The bars showed diabetes risk getting lower as income and education increased.
It was a clean, clear pattern, the more support people had, the healthier they tended to be.

**Final Takeaway**

This whole section shows that health is about more than habits, it’s about circumstances.

Sleeping better helps with weight and blood pressure.

But deeper things like income and education strongly shape your risk for obesity and diabetes.

Health outcomes are linked and social factors like education and income can stack the odds for or against you.

These insights don’t just explain trends, they help us think about how to build healthier communities.

---

### Objective 1.4: How Diet, Exercise, Blood Pressure, and Glucose Affect Our Health

In this part of my project, I explored how our lifestyle—especially what we eat and how active we are—impacts health outcomes like blood pressure, weight (BMI), and cholesterol. I also studied how blood pressure and blood sugar together affect heart disease risk.

#### Systolic Blood Pressure

I first looked at whether diet quality or physical activity levels affect systolic blood pressure.

**What I found:**

There was no significant effect. People with poor diets or low activity didn’t have noticeably different blood pressure. The model couldn’t explain the variation, and the interaction effects weren’t meaningful.

***Plot: Predicted Systolic Blood Pressure by Diet + Activity***

This plot compared systolic blood pressure  across all groups. Visually, the bars are nearly the same height, confirming that lifestyle factors didn’t lead to big differences in systolic blood pressure in this dataset.


#### Body Weight (BMI)

Then, I analyzed BMI, a key measure for weight status.

***What I found:***

People with “Needs Improvement” or “Poor” diets had 3–4 units higher BMI than those with healthy diets.

Moderate activity helped reduce BMI, especially for those with less healthy diets.

***Plot: Predicted BMI by Diet + Activity***

This plot showed how BMI changes across combinations of diet and physical activity. People with poor diets and low activity had the highest BMI, while those who exercised more had noticeably lower BMI—even if their diet wasn’t ideal. It clearly visualizes how moderate physical activity protects against weight gain.

#### Total Cholesterol

I also checked if diet or exercise influenced total cholesterol levels.

**What I found:**

There was no clear pattern—cholesterol didn’t change significantly across diet or activity levels.

***Plot: Predicted Cholesterol by Diet + Activity***

This plot compared total cholesterol across all groups. Visually, the bars are nearly the same height, confirming that lifestyle factors didn’t lead to big differences in cholesterol in this dataset.

#### Cardiovascular Disease (CVD) Risk

Lastly, I looked at how blood pressure and glucose levels together affect the risk of heart disease.

**What I found:**

High blood pressure and high glucose levels were the strongest predictors of heart disease.

Other contributors included: poor diet, low activity, older age, being male, and higher BMI.

Some combinations (like prediabetes with mild hypertension) had slightly lower risk, possibly due to early treatment.

***Plot: Mean Predicted Probability of CVD by BP & Glucose Categories (Weighted)***

This plot visualized predicted probabilities of having cardiovascular disease, based on combinations of blood pressure and glucose categories. It clearly shows that CVD risk increases sharply as both blood pressure and glucose levels get worse.

**My Takeaway**

BMI is the most affected by lifestyle—especially by diet and physical activity.

Blood pressure and cholesterol weren’t influenced much by lifestyle in this analysis—possibly due to medication or other health conditions.

Heart disease risk is highest in people with both high blood pressure and high glucose, but diet, activity, age, and weight also matter.

Even small lifestyle changes—like moving more or improving your diet—can make a real difference in managing weight and long-term heart health.

---

## Goal 2: Uncovering Health Disparities in the U.S.

I wanted to understand how health outcomes can differ based on gender and race or ethnicity, especially when you also consider things like lifestyle and access to resources. So I looked at how habits like diet and physical activity, along with factors like income, education, and health coverage, affect chronic conditions across different groups.

The goal was to see if certain groups are facing more health challenges than others, and why that might be happening. By identifying these differences—also called health disparities—I hoped to better understand what’s driving them and what might help close the gap.

---

### Objective 2.1: Group Comparisons – Exploring Health, Lifestyle & Income Differences Across Gender and Ethnicity

In this section, I wanted to understand how people’s health, habits, and financial situations vary by both gender and race/ethnicity. I used NHANES data to look into things like body weight, blood pressure, diet, sleep, and income. I looked at both the raw (unweighted) numbers and more accurate (weighted) ones that reflect the U.S. population. I’ve explained the patterns mainly using the weighted results, but I’ve included unweighted ones too for context.

**What I Found**

Here’s what stood out to me across the different groups:

#### 1. Body Weight (BMI)

  Non-Hispanic Black women had the highest BMI—around 33—suggesting a higher obesity risk.

  Asian adults, both men and women, had the lowest BMI.

  These same patterns were visible even in the unweighted data.

  ***Plot: BMI by Race and Gender*** – This bar chart clearly showed a racial and gender gap in body weight.

#### 2. Blood Pressure

  Non-Hispanic Black men had the highest blood pressure (both systolic and diastolic), putting them at higher risk of hypertension.

  Mexican American women had the lowest blood pressure readings.

  These differences held true in both weighted and unweighted data.

  ***Plot: Blood Pressure by Group*** – The chart made the disparities in heart health very clear.

#### 3. Cholesterol

  Asian and White women had the highest total cholesterol (~194 mg/dL).

  Non-Hispanic Black adults had the lowest cholesterol levels (~177–181 mg/dL).

  ***Plot: Cholesterol by Gender and Race*** – Gender and racial patterns in cholesterol were easy to spot in this plot.

#### 4. Diet Quality (HEI-2015 Score)

  Asian women had the best diets overall, with HEI scores around 53.

  Non-Hispanic Black men had the lowest diet scores—around 45.

  Across all groups, women generally ate healthier than men.

  ***Plot: HEI Score by Race and Gender*** – You can really see the diet gaps in this one.

#### 5. Sleep Duration

  Mexican American women reported the most sleep—about 8.2 hours per night.

  Multiracial men got the least—just around 7.3 hours.

  In general, women slept more than men in nearly every group.

  ***Plot: Sleep by Race and Gender*** – This one highlighted the gender-based sleep difference clearly.

#### 6. Income (Poverty-Income Ratio or PIR)

  Asian and White adults had the highest PIRs (around 3.3–3.5), meaning they had better financial stability.

  Non-Hispanic Black and Mexican American groups had lower PIRs (around 2.1–2.5), suggesting higher financial stress.

  In almost every group, men earned more than women.

 ***Plot: PIR Distribution and Gender Gap*** – This made income gaps within and between groups very clear.

  Patterns That Held Up Even After Weighting

The weighted results confirmed what the raw numbers suggested. That means these patterns are likely real, not just quirks in the dataset:

- Non-Hispanic Black women consistently had the highest BMI.

- Non-Hispanic Black men had the highest blood pressure.

- Asian adults had the healthiest diets.

- Non-Hispanic Black men had the poorest diet quality.

- Mexican American women slept the most.

**Why Weighting Matters**

NHANES doesn’t just collect random data—it uses a carefully designed sampling method. That means every person in the data actually represents thousands of real people in the U.S. So, while unweighted results are good for quick snapshots, weighted data gives the real picture. That’s why I focused more on those insights when drawing conclusions.

**What This Means for Public Health**

These differences aren’t just numbers—they highlight real opportunities to improve health for everyone:

- ***Support Better Diets*** – Especially for Black and Hispanic men, who are at higher diet risk.

- ***Increase Physical Activity*** – Diet and activity go hand in hand. Programs targeting both can help.

- ***Improve Sleep Education***– Especially for men, who sleep less across all groups.

- ***Tackle Financial Barriers*** – People with lower incomes may need better access to healthy food and care.

- ***Make Health Messaging Inclusive*** – Cultural sensitivity and language access can make a big difference.

**Final Takeaway**

From body mass index to income, the data showed that race, gender, and income all shape health in the U.S. These aren’t just small differences,they’re patterns that demand attention. If we want real progress, we need health strategies that are:

- Targeted to those who need them most
- Inclusive of all cultural backgrounds
- Grounded in real data like this

Better data helps build better solutions—and that’s how we create a healthier, fairer future for everyone.

---

### Objective 2.2 – What Happens When Health Factors Combine?

Sometimes health outcomes don’t just depend on one thing—like income or gender—but how they interact together. So in this section, I looked at how different factors combine and affect health differently for different people. Here's what I found:

#### 1. Does Income Affect Obesity the Same Way for Men and Women?

To find out, I looked at obesity rates based on people’s income levels and gender—together.

**What I found:**

People with low income are more likely to be obese.

But interestingly, low-income men are less likely to be obese than low-income women.

On the other hand, in high-income groups, men are slightly more likely to be obese than women.

So clearly, income affects men and women differently when it comes to obesity. One size doesn’t fit all.

***Plot: Income × Gender → Obesity (Line Plot: Predicted Probability of Obesity and Bar Plot: Predicted Probability of Obesity)*** 

The chart shows how obesity rates shift across income groups for both men and women. It makes it easier to see those differences.

#### 2. Does Sleep Affect BMI Differently Across Racial Groups?

Here, I wanted to see if getting more (or less) sleep affects BMI in different ways for different races or ethnicities.

**What I found:**

Overall, sleep didn’t have a big effect on BMI.

But race and ethnicity still matter. For example, Non-Hispanic Asian people tended to have lower BMI, no matter how much sleep they got.

So while sleep alone doesn’t explain big BMI changes, your background still plays a role in your body weight.

***Plot: Sleep × Race → BMI (Interaction Between Sleep Duration and Race/Ethnicity on BMI and BMI vs. Centered Sleep by Race/Ethnicity)***

One graph shows how BMI changes with sleep for each racial group. Another breaks it down race-by-race so we can see smaller patterns.

#### 3. Does Eating Healthier Help Men and Women’s Cholesterol the Same Way?

This time, I checked if eating better (higher diet score = healthier diet) helps men and women equally when it comes to cholesterol levels.

**What I found:**

Men generally have lower cholesterol than women.

But surprisingly, having a healthier diet didn’t make a big difference in cholesterol—at least not one we could clearly measure.

Also, there wasn’t a big difference in how diet affected cholesterol for men vs. women.

So, diet didn’t seem to have a strong link to cholesterol here. That doesn’t mean it’s not important—just that we didn’t find clear evidence in this data.

***Plot: Diet × Gender → Cholesterol (Predicted Total Cholesterol by Diet Score and Gender and Interaction Plot with 95% CI: Centered Diet Score x Gender -> Total Cholesterol)*** 

The graph shows cholesterol levels for men and women across different diet scores. It’s a nice visual to see trends, even if the differences weren’t huge.

#### 4
. Does a Healthy Diet Lower Diabetes Risk More for Women?

Lastly, I looked at how diet affects the chances of having diabetes, and if that link is different for men and women.

**What I found:**

Better diet = lower risk of diabetes.

Men have slightly higher risk of diabetes than women.

A healthy diet seems to protect women a little more than men.

So yes—eating healthier helps reduce diabetes risk, especially for women.

***Plot: Diet × Gender → Diabetes Risk (Predicted Probability of Diabetes by HEI Score and Gender):*** 

The graph shows how the chances of having diabetes go down as diet gets better, with separate lines for men and women.

### Objective 2.3: Data-Driven Recommendations

- Summary of Key Findings
- Actionable Insights
- Supporting Visuals & Tables
