# -*- coding: utf-8 -*-
"""Richer write-ups per source project number.
q   = framing of the research question (derived from the source brief)
ctx = why the question is interesting (general, well-established knowledge only)
con = key concepts explained (term, explanation) - textbook knowledge, no personal results
app = how the work was approached (logical process consistent with the source; no invented specifics)
emp = why it matters to an employer
Personal results, figures and findings come ONLY from tools/source.md / content.py."""
R = {}
R[1] = dict(
 q="Which fundamentals actually move UK house prices - and how much of the movement can a parsimonious time-series model explain?",
 ctx="House prices sit at the junction of monetary policy, demography and planning constraints. Separating the influence of borrowing costs from population pressure and new supply is the core question for lenders, housebuilders and policymakers alike.",
 con=[("Ordinary least squares (OLS)","Estimates the linear relationship between a dependent variable (here, prices) and several explanatory variables by minimising the sum of squared residuals; each coefficient reads as the effect of a one-unit change holding the others constant."),
      ("R-squared","The share of variation in the dependent variable the model accounts for. A high value in time-series work is a prompt to check for shared trends rather than an automatic sign of a good model."),
      ("Multicollinearity","When explanatory variables move closely together, coefficients become unstable and standard errors inflate. Typically detected with correlation matrices or variance inflation factors (VIFs)."),
      ("Heteroskedasticity","Non-constant error variance. It leaves coefficients unbiased but makes standard errors unreliable, so significance tests can mislead; it is commonly tested with Breusch-Pagan or White tests and handled with robust standard errors."),
      ("Supply-demand equilibrium","Prices settle where housing demand (driven by population and credit conditions) meets a supply that is slow to respond, which is why supply constraints amplify demand shocks.")],
 app=["Framed the hypothesis from theory: higher population density and cheaper credit should raise prices; more supply should restrain them.",
      "Assembled quarterly ONS and Bank of England series for 2005–2019 and aligned them on a common timeline.",
      "Specified and estimated an OLS regression of prices on the chosen determinants.",
      "Interpreted coefficient signs and significance against the theoretical expectations.",
      "Ran diagnostic checks for multicollinearity and heteroskedasticity before relying on the results."],
 emp=["Analyst roles depend on knowing when a model can be trusted. Diagnostics-first regression work is exactly the habit that stops a convincing-looking chart from driving a bad decision on lending, pricing or investment."])
R[2] = dict(
 ctx="Remote work is often discussed as a question of job type or individual skill. This project tested a less visible constraint: whether people have the physical space at home to work at all.",
 con=[("Coefficient interpretation","In a regression, a coefficient measures the expected change in the outcome for a one-unit change in an explanatory variable, holding other factors constant; interpreting it correctly (units, direction, significance) is what turns a model into a usable statement."),
      ("Overcrowding as a constraint","Housing conditions shape whether a quiet, dedicated workspace exists, so they can limit remote working independently of a worker's occupation or qualifications."),
      ("Human capital","Education raises the likelihood of holding knowledge-intensive roles, which are the roles most easily performed away from a workplace.")],
 app=["Defined the outcome (likelihood of working from home) and candidate drivers drawn from labour and housing economics.",
      "Estimated an econometric model relating remote working to overcrowding and education across Greater London.",
      "Interpreted the coefficients in plain terms and tested whether the signs matched the theory.",
      "Critically evaluated what the model can and cannot establish before drawing policy implications."],
 emp=["Employers and public bodies planning hybrid working, office space or housing policy need evidence on who can actually work remotely. Translating a coefficient into a sentence a decision-maker can act on is a core analyst skill."])
R[3] = dict(
 q="How should capital be split across five large-cap shares to get the best return for each unit of risk taken?",
 con=[("Modern Portfolio Theory (MPT)","Markowitz's insight that portfolio risk depends not only on each asset's volatility but on how assets co-move; combining imperfectly correlated assets can lower risk without sacrificing expected return."),
      ("Variance-covariance matrix","Holds every asset's variance and every pairwise covariance; with matrix algebra, portfolio variance is w'Σw, where w is the vector of weights."),
      ("Efficient frontier","The set of portfolios offering the highest expected return for each level of risk. Portfolios below it are dominated: another mix delivers more return for the same risk."),
      ("Sharpe ratio","Excess return over the risk-free rate divided by standard deviation - return per unit of risk. The maximum-Sharpe portfolio is the tangency point between the frontier and the capital market line."),
      ("Linear and non-linear programming with Solver","Excel Solver searches for weights that maximise an objective (the Sharpe ratio) subject to constraints such as weights summing to one.")],
 app=["Collected 2014–2018 share prices for Netflix, Amazon, Google, NVIDIA and RIO and converted them to returns.",
      "Computed mean returns and the variance-covariance matrix, then used matrix algebra to value an equally weighted benchmark portfolio.",
      "Traced the efficient frontier across 10 allocation weightings.",
      "Set up Excel Solver to find the allocation that maximises the Sharpe ratio, and compared it with the equal-weight benchmark."],
 emp=["Risk-adjusted thinking underpins asset management, treasury and corporate finance. Building the frontier from first principles - rather than reading it off a tool - shows the mechanics behind every allocation recommendation."])
R[4] = dict(
 q="Do the two foundational theories of trade - Ricardian comparative advantage and Heckscher-Ohlin factor endowments - actually explain the trade patterns we observe?",
 ctx="Trade theory underpins arguments about tariffs, industrial strategy and which sectors a country should expect to win or lose from openness. If the theories fail empirically, policy built on them inherits the error.",
 con=[("Ricardian model","Trade is driven by differences in labour productivity (technology). Each country gains by specialising in the good it produces at the lowest opportunity cost - comparative, not absolute, advantage."),
      ("Heckscher-Ohlin (H-O) model","Assumes shared technology and explains trade by factor endowments: a country exports goods that use its relatively abundant factor intensively (capital-rich countries export capital-intensive goods)."),
      ("Leontief Paradox","Wassily Leontief's 1953 input-output study found that US exports were less capital-intensive than its import substitutes - the opposite of what H-O predicted for the world's most capital-abundant economy. Proposed explanations include differences in labour skill (human capital), natural resources and trade barriers."),
      ("Heckscher-Ohlin-Vanek (H-O-V)","Generalises H-O to many goods and factors by predicting the factor content of trade: countries should be net exporters of the services of their abundant factors. Empirical tests found weak fit ('missing trade') until technology differences across countries were allowed."),
      ("Theory vs evidence","A recurring lesson: Ricardian productivity differences and H-O endowments each explain part of the picture, and modern work combines them.")],
 app=["Set out the assumptions and predictions of each model side by side.",
      "Reviewed the empirical literature, starting with the Leontief Paradox and the explanations offered for it.",
      "Assessed how H-O-V reframes the test around the factor content of trade.",
      "Weighed where each theory holds and where it breaks down, and concluded on their explanatory validity."],
 emp=["Research and policy roles regularly require judging whether a neat model survives contact with data. This project is a structured example of testing theory against evidence and stating the gap clearly."])
R[5] = dict(
 q="Does AI destroy jobs, or does it reshape which tasks - and which skills - employers pay for?",
 con=[("Task-based model (Acemoglu & Restrepo)","Treats jobs as bundles of tasks. Technology affects labour demand by changing which tasks machines can perform, rather than replacing whole occupations."),
      ("Displacement effect","Automation takes over tasks previously done by workers, reducing labour demand for those tasks."),
      ("Productivity effect","Cheaper production raises output and demand, which can increase labour demand in non-automated tasks and elsewhere in the economy."),
      ("Reinstatement effect","New tasks are created in which labour has a comparative advantage, pulling workers back in. The net effect on employment depends on the balance of all three."),
      ("Skill-biased change","Technology can raise demand for some skills while lowering it for others, so aggregate employment can hold steady while the composition of work changes.")],
 app=["Separated the question into two outcomes: the overall level of employment and the mix of skills demanded.",
      "Used the task-based model to organise the evidence by displacement, productivity and reinstatement effects.",
      "Mapped claims, counter-claims and evidence in a structured argument map before writing.",
      "Wrote a critical essay reaching a reasoned judgement rather than a headline prediction."],
 emp=["Workforce planning, HR strategy and economic consulting all need a disciplined way to discuss technology and jobs. The framework gives a vocabulary for that conversation that goes beyond 'robots take jobs'."])
R[6] = dict(
 q="As production fragments across borders, where is value captured - and what does that mean for developing economies trying to move up?",
 con=[("Global value chains (GVCs) and trade in tasks","Production is split into stages performed in different countries, so countries increasingly trade tasks (assembly, design, logistics) rather than finished goods."),
      ("Smile curve","Plots value added against production stages: high at the ends (R&D, design, branding, after-sales) and low in the middle (manufacturing and assembly). It explains why hosting assembly does not guarantee capturing value."),
      ("Middle-income trap","Economies that grew on low-cost labour can stall when wages rise but they have not yet built the innovation and skills to compete at the high-value ends of the chain."),
      ("Foreign direct investment (FDI)","Can bring capital, technology and market access, but the gains depend on linkages to local firms and on upgrading."),
      ("Supply-chain resilience","Shocks like COVID-19 exposed how tightly optimised, geographically concentrated chains transmit disruption, prompting debate on diversification and reshoring.")],
 app=["Traced how production shifted from national industries to fragmented GVCs.",
      "Used the smile curve to analyse how value is distributed across stages.",
      "Linked GVC participation to development outcomes through FDI and the middle-income trap.",
      "Assessed how global shocks such as COVID-19 tested the resilience of these networks."],
 emp=["Supply-chain, procurement and market-entry decisions hinge on knowing where value and risk sit in a chain. This project builds that map at the level of whole economies."])
R[7] = dict(
 q="How do you judge whether an economy is performing well - and what has to be traded off to improve it?",
 con=[("Core indicators","Real GDP growth (output adjusted for inflation), the unemployment rate, inflation (e.g. CPI) and living-standard measures such as GDP per capita."),
      ("Macroeconomic objectives","Policy typically pursues stable growth, low unemployment, price stability and a sustainable external balance; these goals can pull against each other."),
      ("Phillips curve","Describes a short-run inverse relationship between unemployment and inflation. Expectations-augmented versions (Friedman, Phelps) imply no permanent trade-off, and the relationship has shifted and flattened over time."),
      ("Comparative analysis","Comparing economies on the same indicators separates global shocks from country-specific policy choices.")],
 app=["Defined the indicator set and what each reveals about economic health.",
      "Evaluated the four pillars of macroeconomic policy and the tensions between them.",
      "Compared performance across different economies on common measures.",
      "Used the Phillips curve to analyse the trade-off between inflation and unemployment."],
 emp=["Economic, credit and market-risk teams translate indicator releases into a view on conditions. This project practises that translation, from numbers to narrative to risk."])
R[8] = dict(
 q="When inflation spikes, how do central banks restore price stability - and who bears the cost in jobs and incomes?",
 con=[("Supply vs demand shocks","Demand-driven inflation responds well to tighter policy; supply shocks (such as energy prices) raise inflation while weakening output, making the policy choice harder."),
      ("Inflation targeting","Central banks such as the Bank of England set interest rates to bring inflation back to target, relying on credibility to anchor expectations."),
      ("Transmission mechanism","Rate rises work through borrowing costs, asset prices, the exchange rate and expectations, with long and variable lags."),
      ("Distributional effects","Inflation and the response to it fall unevenly: lower-income households spend more on essentials, while borrowers, savers and workers in rate-sensitive sectors are affected differently.")],
 app=["Characterised the recent inflation shocks and their sources.",
      "Examined how central banks responded to protect price stability.",
      "Evaluated the knock-on effects of those interventions on employment and income inequality.",
      "Drew the analysis together in a critical essay."],
 emp=["Interest-rate decisions feed directly into pricing, wage settlements, credit risk and hiring plans. Understanding the policy reaction function helps an organisation anticipate rather than react."])
R[9] = dict(
 q="What should government do about soaring energy bills - and should energy producers' extraordinary profits help pay for it?",
 con=[("Windfall tax","A one-off or temporary tax on profits judged to arise from external events rather than firm effort or investment. The argument is that taxing such rents distorts behaviour less; the counter-argument is that it can deter future investment and raise policy uncertainty."),
      ("Targeted vs universal support","Universal measures (such as price caps) are simple but costly and poorly targeted; targeted payments are cheaper per household helped but risk gaps in coverage."),
      ("Fuel poverty and demographic variation","Energy use and vulnerability differ by age, household type, housing quality and income, so the same price shock hits groups unevenly.")],
 app=["Took the role of a junior economist writing for the Secretary of State, so prioritised clarity and actionable options.",
      "Evaluated the main policy responses to rising energy costs.",
      "Reviewed energy producers' financial data for 2014–2023 to inform the windfall-tax debate.",
      "Researched how fuel consumption varies across demographic groups to identify who is most exposed.",
      "Condensed the evidence into a high-level briefing with ethical considerations made explicit."],
 emp=["Briefing senior decision-makers on a contested issue - with financial evidence, distributional analysis and a clear recommendation on one page - is the core output of policy, public affairs and strategy roles."])
R[10] = dict(
 q="What do developed nations owe developing nations that bear climate damage they did little to cause?",
 con=[("Climate externality","Emissions impose costs on others who are not party to the decision; climate change is a global negative externality, with costs borne disproportionately by low-emitting countries."),
      ("Climate justice","Frames responsibility in terms of historical emissions and capacity to pay, not only current emissions."),
      ("Loss and damage","Covers climate harms that adaptation cannot prevent. A dedicated fund was agreed at COP27 in 2022, but scale, contributors and eligibility remain contested."),
      ("Climate-induced migration","Displacement from rising seas, flooding and extreme weather carries long-term economic and social costs and has weak legal protection.")],
 app=["Compared Bangladesh (densely populated, flood-exposed) and Tuvalu (a low-lying island state facing existential sea-level risk) as contrasting cases.",
      "Evaluated the loss and damage framework against the principles of climate justice.",
      "Examined the political barriers to financing it and the long-run costs of climate-induced migration."],
 emp=["ESG, sustainable finance and international development roles require reasoning about externalities and responsibility, not just emissions numbers. This project frames climate as an economic allocation problem."])
R[11] = dict(
 q="Is there an economic case for state investment banks - and when do they add something private finance cannot?",
 con=[("Market failure","Private markets under-supply some investment, for example because of information problems, long horizons or risks that private lenders will not hold."),
      ("Externalities and public goods","Investments with wide social spill-overs (infrastructure, basic research, green energy) earn private returns below their social value, so they are under-financed."),
      ("Countercyclical lending","Private credit contracts in downturns; public banks can maintain or expand lending to stabilise investment through the cycle."),
      ("The entrepreneurial state (Mazzucato)","Argues that the state has often been the early, risk-taking investor behind major technologies, shaping and creating markets rather than merely fixing their failures.")],
 app=["Set out the market-failure rationale for public banks.",
      "Assessed their role in financing externalities and public goods.",
      "Evaluated their countercyclical lending role during recessions.",
      "Contrasted market-fixing and market-shaping (entrepreneurial-state) views of public investment."],
 emp=["Public finance, infrastructure, development banking and strategy roles increasingly involve co-investment between public and private sectors. Knowing the economic logic for each side's role makes those partnerships easier to structure and justify."])
R[12] = dict(
 q="Did today's rich economies protect their young industries on the way up - and does that hold lessons for trade policy now?",
 con=[("Infant industry argument","Associated with Alexander Hamilton and Friedrich List: new industries may need temporary protection until they reach the scale and learning needed to compete with established foreign rivals."),
      ("Learning-by-doing and scale economies","The mechanism behind the argument: costs fall with experience and volume, so a protected period can be efficient if it ends."),
      ("Risks of protection","Protection can become permanent, shelter inefficiency and invite retaliation; the argument depends on credible exit and good selection."),
      ("Correlation vs causation","A link between trade regimes and growth across periods may reflect other factors (global demand, technology, policy mixes), so the evidence needs careful interpretation.")],
 app=["Built a historical comparison of protectionist measures in the UK, USA, Germany and Japan during early industrialisation.",
      "Compared the 1960–1980 protection period with the 1980–2000 liberalisation period.",
      "Tested the correlation between trade policy stance and GDP growth across the two periods.",
      "Interpreted the results against the risks of protection and the limits of correlational evidence."],
 emp=["Emerging-market analysis and international strategy need context-sensitive views on trade policy rather than one-size-fits-all rules. This project combines history and data to build that judgement."])
R[13] = dict(
 q="What happens when essential water services are run on market principles - and who loses when efficiency and equity collide?",
 con=[("Neoclassical policy toolkit","Privatisation, market-based (cost-reflective) pricing and deregulation, justified by the expectation that competition and price signals allocate resources efficiently."),
      ("Natural monopoly","Water networks have high fixed costs and are uneconomic to duplicate, so privatisation tends to create private monopolies rather than competition, which makes regulation essential."),
      ("Efficiency vs equity","Prices that reflect cost can improve efficiency but make an essential good less affordable for low-income households, a tension sharper for water than for most goods."),
      ("Regulatory responses","Price caps, social tariffs and service obligations are the usual tools for protecting vulnerable users.")],
 app=["Set out the neoclassical case for privatisation, market pricing and deregulation.",
      "Assessed how those principles fit water, an essential good with natural-monopoly features.",
      "Reviewed the literature on the efficiency-equity trade-off.",
      "Investigated the impact of private monopolies on low-income and marginalised communities."],
 emp=["Regulators, utilities, PPP advisers and ESG teams all have to weigh commercial efficiency against social obligations. This project rehearses that trade-off on one of the most politically sensitive sectors."])
R[14] = dict(
 con=[("Return on capital employed (ROCE)","Operating profit divided by capital employed: how efficiently a business turns its long-term funding into profit, central when a club invests heavily in a stadium."),
      ("Current ratio","Current assets divided by current liabilities: a measure of short-term liquidity and the ability to meet near-term obligations."),
      ("Gearing","Debt relative to equity or capital: the degree to which a business relies on borrowing, and therefore its exposure to interest costs and refinancing risk."),
      ("Wage-to-turnover ratio","A key football-finance metric: high ratios leave little margin for other costs and signal pressure under spending rules."),
      ("Price inelasticity","When demand barely responds to price, as for loyal matchday supporters, revenue can rise with price, though at a reputational cost."),
      ("Profit and Sustainability Rules (PSR)","Premier League rules limiting losses over a rolling period, linking on-pitch spending to financial discipline.")],
 emp=["The same toolkit - ratio analysis, benchmarking and reading ownership and capital-project risk - transfers directly to credit analysis, equity research and corporate finance in any sector."])
R[15] = dict(
 q="How can a club with a distinctive identity turn that identity into a lasting competitive advantage and commercial growth?",
 con=[("PESTEL","Scans the Political, Economic, Social, Technological, Environmental and Legal forces acting on an organisation."),
      ("Porter's Five Forces","Assesses industry attractiveness through rivalry, the threat of new entrants and substitutes, and buyer and supplier power."),
      ("VRIO","Tests internal resources for Value, Rarity, Inimitability and Organisation; only resources meeting all four sustain a competitive advantage."),
      ("STP","Segmentation, Targeting and Positioning: divide the market, choose which segments to serve, and define how the brand should be perceived by them.")],
 app=["Mapped the external environment with PESTEL and Porter's Five Forces.",
      "Audited internal resources with VRIO to identify which could underpin sustained advantage.",
      "Built the marketing plan through STP, linking chosen segments to the club's environmental positioning.",
      "Drew the analysis into a 4,000-word strategic roadmap."],
 emp=["Strategy and brand roles in any industry use the same sequence: understand the environment, identify defensible resources, then target the customers who value them. This project runs the full sequence end to end."])
R[16] = dict(
 q="How does a Chief People Officer turn a diverse workforce into a genuinely inclusive culture that performs?",
 con=[("Diversity vs inclusion","Diversity describes who is in the organisation; inclusion describes whether they can contribute fully. Benefits depend on the second, not only the first."),
      ("Emotional intelligence (EI)","Models such as Goleman's emphasise self-awareness, self-regulation, motivation, empathy and social skill as drivers of leadership effectiveness."),
      ("Multi-generational dynamics","Different generations can bring different expectations about communication, feedback and flexibility, a potential source of conflict or of complementary strengths."),
      ("Cognitive synergy","The performance gain when varied perspectives are combined effectively rather than suppressed.")],
 app=["Took the strategic perspective of a Chief People Officer.",
      "Reviewed emotional intelligence models as a basis for inclusive leadership.",
      "Investigated multi-generational workforce dynamics and sources of conflict.",
      "Proposed an organisational framework designed to minimise conflict and build cognitive synergy."],
 emp=["People analytics, HR strategy and management roles need a structured view of culture as a performance lever. The project frames human capital as a strategic asset."])
R[17] = dict(
 q="Where does the way I see myself as a leader differ from how others see me - and what should I do about the gaps?",
 con=[("Johari Window","A 2×2 model (Luft and Ingham) with four areas - open, blind, hidden and unknown - formed by what is known to oneself and what is known to others. Feedback shrinks the blind area; self-disclosure shrinks the hidden one."),
      ("Goleman's emotional intelligence framework","Self-awareness, self-regulation, motivation, empathy and social skills as the competencies behind effective leadership."),
      ("Development planning","Turning feedback into specific, time-bound actions that can be reviewed.")],
 app=["Gathered self-assessment and peer feedback on leadership traits.",
      "Placed the results in the Johari Window to separate shared strengths from blind spots.",
      "Interpreted the gaps through Goleman's EI competencies.",
      "Designed a structured personal professional development plan from the findings."],
 emp=["Employers look for analysts who seek feedback and act on it. This project demonstrates that habit through a recognised framework."])
R[18] = dict(
 con=[("AIDA model","Attention, Interest, Desire, Action: a funnel describing how communication moves an audience from awareness to behaviour, used here to locate where fans drop out between online engagement and turning up."),
      ("Technology Acceptance Model (TAM)","Adoption of a technology depends on perceived usefulness and perceived ease of use, which explains why clunky club websites and ticketing lose would-be attendees."),
      ("Thematic analysis","A qualitative method of coding interview data and grouping codes into themes, which makes unstructured conversations comparable and defensible."),
      ("Mixed methods","Combining qualitative themes with quantitative scores so that each validates and explains the other.")],
 emp=["Conversion-funnel thinking and mixed-methods research are the same tools used in marketing analytics, CX and product research. Here they are applied under the tight budget constraints most organisations actually face."])
R[19] = dict(
 con=[("Contribution margin and break-even","Contribution is price minus variable cost per participant; break-even volume is fixed costs divided by contribution. Testing several price points shows how sensitive viability is to pricing."),
      ("Market sizing","Estimating the addressable population from official data (here ONS Census 2021) before forecasting uptake."),
      ("Weighted multi-criteria decision analysis (MCDA)","Scores options against several criteria, weighted by importance, so that a decision with competing objectives becomes transparent."),
      ("Sensitivity analysis","Re-running the ranking under many randomised weightings tests whether the recommendation depends on a particular set of assumptions."),
      ("Sampling bias","When a survey reaches a different population from the target one, conclusions about the target are unreliable. Recognising this is as important as the data itself.")],
 emp=[])
R[20] = dict(
 q="Which audiences and channels are actually converting - and where should the advertising budget go next?",
 con=[("Conversion rate","The share of an audience completing a desired action. Comparing it across channels and segments shows where spend works."),
      ("Multi-channel attribution","Customers often see several channels before converting, so judging each channel's contribution requires care."),
      ("Segmentation","Splitting customers into audiences reveals differences that an overall average hides.")],
 app=["Clarified the client's goals before touching the data.",
      "Interpreted simulated customer behaviour data in Excel by audience and channel.",
      "Compared conversion trends across segments to identify strong and weak performers.",
      "Framed data-backed recommendations aligned to the client's objectives."],
 emp=["It mirrors the weekly rhythm of a marketing analytics team: segment, compare, recommend."])
R[21] = dict(
 q="How do you turn raw corporate records into a classified, trustworthy dataset - and then into a dashboard someone can use?",
 con=[("Data classification","Assigning records to consistent categories so that they can be counted, compared and audited."),
      ("Data modelling","Structuring data into related tables and fields so that analysis tools can aggregate it correctly."),
      ("Forensic technology","Using data analysis to detect anomalies, irregularities or risk in corporate records."),
      ("Interactive dashboards","Filters and drill-downs that let users explore the data themselves rather than read a static report.")],
 app=["Cleaned and classified raw corporate records in Excel.",
      "Structured the data for analysis.",
      "Built an interactive visualisation dashboard in Tableau."],
 emp=["The clean-model-visualise workflow is the daily work of audit analytics, BI and consulting data teams."])
R[22] = dict(
 q="What does an executive need to see - and what should be asked before they see it?",
 con=[("Data storytelling","Choosing the chart, ordering and annotation so that the key message is obvious to a time-poor audience."),
      ("Chart selection","Matching the visual to the question (trend, comparison, composition, distribution) to avoid misleading reads."),
      ("Requirements framing","Drafting the business questions first ensures that the visuals answer what the client actually needs to decide.")],
 app=["Drafted strategic questions to prepare for a client alignment meeting.",
      "Cleaned retail revenue datasets.",
      "Built executive-level visuals in Tableau and Power BI to answer those questions."],
 emp=["Executive reporting succeeds or fails on clarity. This simulation practises building visuals for a senior audience under a consulting brief."])
R[23] = dict(
 q="Which assumptions is a luxury clothing brand making about its revenue - and what happens if they are challenged?",
 con=[("Assumption busting","Listing the beliefs a business takes for granted and deliberately inverting them to open new options."),
      ("Structured brainstorming","Facilitation techniques that generate many ideas before evaluating them, then filter for commercial viability."),
      ("Repositioning","Changing how a brand is perceived or which customers it targets in order to unlock growth.")],
 app=["Identified the brand's underlying business assumptions.",
      "Applied structured creative-thinking techniques to challenge them.",
      "Facilitated brainstorming on revenue optimisation and market repositioning.",
      "Screened the ideas for commercial viability."],
 emp=["Consulting and strategy roles reward people who can question a client's frame without losing commercial realism."])
R[25] = dict(
 q="How do you take messy operational data from a database all the way to a dashboard a manager can trust?",
 con=[("Relational databases and joins","Data is stored in related tables; joins recombine them on shared keys, and the choice of join type determines which records survive."),
      ("ETL","Extract, Transform, Load: pulling data from sources, cleaning and reshaping it, and loading it where it can be analysed."),
      ("Descriptive statistics","Means, medians, spread and counts that summarise data and catch anomalies before visualisation."),
      ("BI data modelling","Defining the relationships between tables inside Power BI or Tableau so that filters and measures aggregate correctly.")],
 emp=["Most analyst roles span exactly this chain. Being able to own it end to end means fewer hand-offs and fewer places for errors to creep in."])
