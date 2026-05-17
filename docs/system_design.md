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


![System Architecture](../3.4%20Architecture_diagram.png)

# 3.5 Human Judgment and Automation Boundaries

The proposed system does not fully automate final lending governance decisions. While the AI model can evaluate credit risk, detect fairness concerns, and apply jurisdiction-specific governance rules, certain high-risk decisions still require human oversight.

In the European Union, high-risk AI systems are subject to stricter governance obligations under the EU AI Act. Therefore, lending decisions involving insufficient explainability, potential demographic bias, or unusually high-risk classifications are escalated for manual review. Human reviewers are responsible for assessing whether the AI-generated decision is reasonable, explainable, and compliant with regulatory expectations.

In the United States, the system primarily supports compliance documentation and fair lending monitoring. However, human intervention may still be required when the system detects potential discrimination risks or incomplete explanation records.

This governance boundary is intended to reduce overreliance on automated decision-making while improving accountability and regulatory transparency across jurisdictions.

# 3.6 Failure Modes and Governance Risks

Several governance and operational risks may affect the proposed jurisdiction-aware AI lending governance system.

First, regulatory rules may change over time. The governance engine could apply outdated jurisdiction logic if regulatory updates are not incorporated promptly. This may lead to incorrect compliance assessments or insufficient governance controls.

Second, AI model drift may reduce the reliability of credit scoring outcomes. Changes in applicant behaviour, economic conditions, or data distributions could gradually weaken model accuracy and fairness performance.

Third, explainability mechanisms may not always provide sufficiently transparent decision explanations for complex AI models. This could create governance challenges under stricter EU regulatory requirements for high-risk AI systems.

Fourth, jurisdiction detection errors may apply incorrect governance rules to cross-border lending cases. This may result in inconsistent compliance treatment between the United States and the European Union.

Finally, excessive reliance on automated governance workflows may reduce meaningful human oversight. Human reviewers may gradually over-trust AI-generated compliance outputs without critically evaluating the underlying decision logic.

These risks demonstrate that jurisdiction-aware AI governance systems require continuous monitoring, regulatory updating, and human supervision rather than fully autonomous operation.

# 3.7 Example Governance Outputs

The proposed system generates different governance outcomes depending on the jurisdiction and risk profile of the lending decision.

Possible governance outputs include:

- COMPLIANT  
  The lending decision satisfies applicable jurisdiction-specific governance requirements.

- HUMAN_REVIEW_REQUIRED  
  The system detects high-risk conditions such as insufficient explainability, demographic bias concerns, or incomplete compliance documentation.

- HIGH_RISK_AI_WARNING  
  The lending model may trigger stricter governance obligations under the EU AI Act due to limited transparency or elevated fairness risks.

- FAIR_LENDING_ALERT  
  Potential discrimination or fairness concerns are identified under US fair lending requirements.

- REGULATORY_CONFIGURATION_WARNING  
  Jurisdiction rules or governance parameters may be outdated or inconsistently applied.

  # 3.8 Limitations and Future Improvements

The current prototype is designed as a governance architecture demonstration rather than a production-ready AI lending platform.

Several technical and operational components are simplified within the current project scope. First, the system does not implement live financial data integration or real-time machine learning deployment. The lightweight Python prototype is intended only to demonstrate jurisdiction-aware governance logic.

Second, the explainability and fairness assessment mechanisms are conceptual rather than fully model-driven. Advanced explainable AI methods such as SHAP or LIME are not implemented in the current prototype.

Third, the governance workflow currently focuses only on regulatory divergence between the United States and the European Union. Additional jurisdictions such as the United Kingdom, Singapore, or Canada may be incorporated in future development.

Finally, the current system focuses primarily on governance orchestration and compliance logic rather than predictive model optimisation or commercial lending performance.

Despite these limitations, the project demonstrates how jurisdiction-aware governance architecture can improve transparency, accountability, and cross-border AI lending compliance management.
