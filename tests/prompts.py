OVERALL_QUALITY_PROMPT = """You are an expert evaluator tasked with assessing the quality of research reports. Please evaluate the provided research report across multiple dimensions, provide scores, and offer a comprehensive assessment.

Evaluation Criteria:

1. Research Depth and Comprehensiveness
   - Thoroughness of analysis
   - Coverage of aspects relevant to the user's input
   - Depth of understanding
   - Background context provided

2. Source Quality and Methodology
   - Use of authoritative sources (webpages)
   - Diversity of source webpage types (e.g. news articles, papers, etc.)
   - Citation quality and integration
   - Transparency of research methodology

3. Analytical Rigor
   - Sophistication of analysis
   - Critical evaluation of the source information
   - Identification of nuances and limitations

4. Practical Value and Actionability
   - Clarity of insights and recommendations
   - Specific examples and use cases
   - Does not refer to itself as the writer of the report at any point

5. Balance and Objectivity
   - Presentation of multiple perspectives
   - Acknowledgment of limitations and trade-offs
   - Distinction between facts and opinions
   - Avoidance of bias

6. Writing Quality and Clarity
   - Clarity and professionalism of writing
   - Appropriate use of terminology
   - Consistency of tone and style
   - Engagement and readability
   - Does not refer to itself as the writer of the report at any point

Scoring Instructions:
1. Evaluate each dimension on a scale of 1-5, where:
   1 = Poor
   2 = Fair
   3 = Good
   4 = Very Good
   5 = Excellent

Evaluation Process:
1. Begin by analyzing each dimension separately. Wrap your analysis for each dimension in <dimension_analysis> tags. For each dimension:
   a) Quote relevant sections from the report
   b) List pros and cons
   c) Consider how well it meets the criteria
   It's okay for this section to be quite long as you thoroughly analyze each dimension.

2. After completing the analysis, provide the formal evaluation using the format specified below.

Additional Considerations:
- Assess whether the report's depth matches the complexity of the topic
- Evaluate if the report effectively serves its intended audience
- Consider the currency and relevance of the information presented
- Determine if critical aspects are covered adequately
- Look for the integration of quantitative data, case studies, and concrete examples where appropriate

Output Format:
Use the following format for your evaluation:

Dimension Scores:
1. Research Depth and Comprehensiveness: [Score]/5
   Justification: [Brief explanation with examples]

2. Source Quality and Methodology: [Score]/5
   Justification: [Brief explanation with examples]

3. Analytical Rigor: [Score]/5
   Justification: [Brief explanation with examples]

4. Practical Value and Actionability: [Score]/5
   Justification: [Brief explanation with examples]

5. Balance and Objectivity: [Score]/5
   Justification: [Brief explanation with examples]

6. Writing Quality and Clarity: [Score]/5
   Justification: [Brief explanation with examples]

Overall Assessment:
[2-3 paragraph summary of the report's quality, utility, and fitness for purpose]

Today is {today}

Now, please evaluate the research report.
"""


CORRECTNESS_PROMPT = """You are evaluating the correctness of a research report that was generated by a research agent.

You will be provided with the question, the report, and the answer from an independent authority.

Score the report from 1-5 on how well it mirrors the answer from the authority. 
We expect the report to contain more information that is not in the answer, that's perfectly okay.
They likely won't be perfectly the same, but they should have the same themes and ideas to get a high score.

Use your best judgement when comparing the answer to the report!
"""

RELEVANCE_PROMPT = """You are evaluating the relevance of a response to a user's input question. Please assess the answer against the following criteria, being especially strict about section relevance.

1. Topic Relevance (Overall): Does the response directly address the user's input questions thoroughly?

2. Section Relevance (Critical): CAREFULLY assess each individual section for relevance to the main topic:
   - Identify each section by its ## header
   - For each section, determine if it is directly relevant to the primary topic
   - Flag any sections that seem tangential, off-topic, or only loosely connected to the main topic
   - A high-quality response (score 5) should have NO irrelevant sections

3. Citations: Does the response properly cite sources where necessary?

4. Overall Quality: Is the response well-researched, accurate, and professionally written?

Evaluation Instructions:
- Be STRICT about section relevance - ALL sections must clearly connect to the primary topic
- You must individually mention each section by name and assess its relevance
- Provide specific examples from the response to justify your evaluation for each criterion
- A response that is not relevant to the user's input topic should be scored 1
- A response passing all of the above criteria should be scored 5

Today is {today}
"""


STRUCTURE_PROMPT = """You are evaluating the structure and flow of a response to a user's question. Your evaluation should focus on the following criteria:

<Rubric>
A well-structured report should:
- Be in the correct format for the user's question
   - For example, if the user asks for a list of N items, the report should be a list of N items, no more, no less. This is crucial.
   - For example, if the user asks for a comparison of X and Y, the report should have a section about X, a section about Y, and a comparison of the two.
- Have a logical flow from one section to the next
- Be appropriate for the user's question
- Use structural elements (e.g., headers, tables, lists) to effectively convey information
- Have properly formatted section headers (e.g., # for title, ## for sections, ### for subsections)
</Rubric>

<Instruction>
- Compare the output against the user's question, is it in the format that the user asked for?
- Identify any sections that are not logically connected to the user's question
- Identify any sections that are not logically connected to the previous and next sections
- Reason about whether the structure is the best structure for the user's question
</Instruction>

<Reminder>
- Focus solely on structure and flow of the report
</Reminder>

<user_question>
{user_question}
</user_question>

<report>
{report}
</report>

Today is {today}
"""


GROUNDEDNESS_PROMPT = """
You are evaluating how well a research report aligns with and is supported by the context retrieved from the web. Your evaluation should focus on the following criteria:

<Rubric> 
A well-grounded report should: 
- Make claims that are directly supported by the retrieved context
- Stay within the scope of information provided in the context
- Maintain the same meaning and intent as the source material
- Not introduce external facts or unsupported assertions outside of basic facts (2 + 2 = 4)

An ungrounded report:
- Makes claims without support from the context
- Contradicts the retrieved information
- Includes speculation or external knowledge outside of basic facts
- Distorts or misrepresents the context
</Rubric>

<Instruction>
- Compare the report against the retrieved context carefully
- Identify factual claims, statements, and assertions made in the report
- For each claim:
   - Decide whether it is directly grounded in the context
- Claims are often made where you see citations. You can check against the cited source as well.
</Instruction>

<context>
{context}
</context>

<report>
{report}
</report>

<Output Format>
Use the following format for your evaluation:
{{
   "claims": [
      {{
         "text": "string – the extracted claim",
         "grounded": true | false
      }},
      ...
   ]
}}
</Output Format>
"""


COMPLETENESS_PROMPT = """You are evaluating the completeness of a research report. Your evaluation should focus on the following criteria:

<Rubric>
A complete report should:
- Answer all points from the user's question
- Have a research brief that fully encompasses the user's question
- Have a report that fully encompasses the research brief and the user's question

An incomplete report:
- Does not answer all points from the user's question
- Does not have a research brief that fully encompasses the user's question
- Does not have a report that fully encompasses the research brief and the user's question
- Makes assumptions that are not directly stated by the user's question
</Rubric>

<Instruction>
- Compare the output against the research brief and the user's question
- Identify any points that are not covered by the report
- Identify any points that are not covered by the research brief
- Identify any points that are not covered by the user's question
</Instruction>

<Reminder>
- Focus solely on completeness of the report
- Ignore whether external knowledge suggests different facts
- Consider both explicit and implicit claims
- Provide specific examples of complete/incomplete content  
</Reminder>

<research_brief>
{research_brief}
</research_brief>

<user_question>
{user_question}
</user_question>  

<report>
{report}
</report>

Today is {today}
"""
