# 3.1 Problem Statement
AI-driven lending systems are increasingly used by multinational financial institutions to automate credit scoring and improve operational efficiency. However, AI governance requirements differ significantly across jurisdictions. In the United States, regulators mainly focus on fair lending outcomes and anti-discrimination obligations, while the European Union additionally emphasises transparency, explainability, and human oversight under the EU AI Act.

These regulatory differences create governance complexity for cross-border financial institutions such as Klarna. Manual review processes and spreadsheet-based monitoring systems are often insufficient to manage rapidly changing regulatory requirements across multiple jurisdictions. Therefore, this project proposes a jurisdiction-aware AI lending governance tool that applies different compliance logic depending on the applicable regulatory environment.

# 3.2 System Objectives
The proposed system is designed to support cross-border AI lending governance through jurisdiction-aware compliance logic.
- Detect jurisdiction-specific regulatory requirements.
- Apply different governance rules for the US and EU.
- Support explainability and auditability of AI decisions.
- Trigger human review for high-risk lending outcomes.
- Identify potential fairness and discrimination risks.
- Improve governance consistency across jurisdictions.

# 3.3 Jurisdiction Logic Matrix

| Governance Scenario | United States | European Union |
|---|---|---|
| Fully automated loan rejection | Allowed if adverse action notice is provided | Human review may be required under the EU AI Act |
| Low explainability AI model | Compliance warning | High-risk AI concern |
| Bias detected in lending outcomes | Fair lending investigation risk | Governance escalation and documentation required |
| Missing decision explanation | Operational warning | Potential non-compliance for high-risk AI systems |
| High-risk applicant classification | Additional monitoring recommended | Mandatory governance safeguards |

# 3.4 System Architecture

The proposed system applies jurisdiction-aware governance logic to AI-driven lending decisions across the United States and the European Union.

The governance workflow consists of several key components:

1. Input Layer  
   Receives applicant information, AI-generated credit scores, confidence levels, and explanation data.

2. Jurisdiction Detection Layer  
   Identifies whether the lending decision falls under US or EU regulatory requirements.

3. Governance Rules Engine  
   Applies jurisdiction-specific governance logic based on regulatory obligations.

4. Bias and Explainability Assessment  
   Evaluates potential fairness risks and checks whether sufficient decision explanations are available.

5. Human Review Trigger  
   Escalates high-risk or insufficiently explainable cases for manual review.

6. Compliance Output Layer  
   Generates governance outcomes such as COMPLIANT, HIGH_RISK, or HUMAN_REVIEW_REQUIRED.
