<!-- page: 1 -->

# Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

This publication is available free of charge from: [https://doi.org/10.6028/NIST.AI.600-1](https://doi.org/10.6028/NIST.AI.600-1)

<!-- page: 2 -->

**NIST Trustworthy and Responsible AI NIST AI 600-1**

# Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile

This publication is available free of charge from: [https://doi.org/10.6028/NIST.AI.600-1](https://doi.org/10.6028/NIST.AI.600-1)

July 2024

![](images/page_1_image_4.jpg)

U.S. Department of Commerce Gina M. Raimondo, Secretary

National Institute of Standards and Technology Laurie E. Locascio, NIST Director and Under Secretary of Commerce for Standards and Technology

<!-- page: 3 -->

**About AI at NIST**: The National Institute of Standards and Technology (NIST) develops measurements, technology, tools, and standards to advance reliable, safe, transparent, explainable, privacy-enhanced, and fair artificial intelligence (AI) so that its full commercial and societal benefits can be realized without harm to people or the planet. NIST, which has conducted both fundamental and applied work on AI for more than a decade, is also helping to fulfill the 2023 Executive Order on Safe, Secure, and Trustworthy AI. NIST established the U.S. AI Safety Institute and the companion AI Safety Institute Consortium to continue the efforts set in motion by the E.O. to build the science necessary for safe, secure, and trustworthy development and use of AI.

**Acknowledgments:** This report was accomplished with the many helpful comments and contributions from the community, including the NIST Generative AI Public Working Group, and NIST staff and guest researchers: Chloe Autio, Jesse Dunietz, Patrick Hall, Shomik Jain, Kamie Roberts, Reva Schwartz, Martin Stanley, and Elham Tabassi.

## NIST Technical Series Policies

[Copyright, Use, and Licensing Statements](https://doi.org/10.6028/NIST-TECHPUBS.CROSSMARK-POLICY) [NIST Technical Series Publication Identifier Syntax](https://www.nist.gov/nist-research-library/nist-technical-series-publications-author-instructions#pubid)

## Publication History

Approved by the NIST Editorial Review Board on 07-25-2024

## Contact Information

[ai-inquiries@nist.gov](mailto:ai-inquiries@nist.gov)

National Institute of Standards and Technology Attn: NIST AI Innovation Lab, Information Technology Laboratory 100 Bureau Drive (Mail Stop 8900) Gaithersburg, MD 20899-8900

## Additional Information

Additional information about this publication and other NIST AI publications are available at [https://airc.nist.gov/Home.](https://airc.nist.gov/Home)

Disclaimer: Certain commercial entities, equipment, or materials may be identified in this document in order to adequately describe an experimental procedure or concept. Such identification is not intended to imply recommendation or endorsement by the National Institute of Standards and Technology, nor is it intended to imply that the entities, materials, or equipment are necessarily the best available for the purpose. Any mention of commercial, non-profit, academic partners, or their products, or references is for information only; it is not intended to imply endorsement or recommendation by any U.S. Government agency.

<!-- page: 4 -->

## Table of Contents

- 1. Introduction ...... 1
- 2. Overview of Risks Unique to or Exacerbated by GAI ...... 2
- 2.1. CBRN Information or Capabilities ...... 5
- 2.2. Confabulation ...... 6
- 2.3. Dangerous, Violent, or Hateful Content ...... 6
- 2.4. Data Privacy ...... 7
- 2.5. Environmental Impacts ...... 8
- 2.6. Harmful Bias and Homogenization ...... 8
- 2.7. Human-AI Configuration ...... 9
- 2.8. Information Integrity ...... 9
- 2.9. Information Security ...... 10
- 2.10. Intellectual Property ...... 11
- 2.11. Obscene, Degrading, and/or Abusive Content ...... 11
- 2.12. Value Chain and Component Integration ...... 12
- 3. Suggested Actions to Manage GAI Risks ...... 12
- Appendix A. Primary GAI Considerations ...... 47
- Appendix B. References ...... 54

<!-- page: 5 -->

## 1. Introduction

This document is a cross-sectoral profile of and companion resource for the [AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) (AI RMF 1.0) for Generative AI,<sup>1</sup> pursuant to President Biden’s Executive Order (EO) 14110 on Safe, Secure, and Trustworthy Artificial Intelligence.<sup>2</sup> The AI RMF was released in January 2023, and is intended for voluntary use and to improve the ability of organizations to incorporate trustworthiness considerations into the design, development, use, and evaluation of AI products, services, and systems.

A [profile](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Core_And_Profiles/6-sec-profile) is an implementation of the AI RMF functions, categories, and subcategories for a specific setting, application, or technology – in this case, Generative AI (GAI) – based on the requirements, risk tolerance, and resources of the Framework user. AI RMF profiles assist organizations in deciding how to best manage AI risks in a manner that is well-aligned with their goals, considers legal/regulatory requirements and best practices, and reflects risk management priorities. Consistent with other AI RMF profiles, this profile offers insights into how risk can be managed across various stages of the AI lifecycle and for GAI as a technology.

As GAI covers risks of models or applications that can be used across use cases or sectors, this document is an AI RMF cross-sectoral profile. Cross-sectoral profiles can be used to govern, map, measure, and manage risks associated with activities or business processes common across sectors, such as the use of large language models (LLMs), cloud-based services, or acquisition.

This document defines risks that are novel to or exacerbated by the use of GAI. After introducing and describing these risks, the document provides a set of suggested actions to help organizations govern, map, measure, and manage these risks.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">1 EO 14110 defines Generative AI as “the class of AI models that emulate the structure and characteristics of input data in order to generate derived synthetic content. This can include images, videos, audio, text, and other digital content.” While not all GAI is derived from foundation models, for purposes of this document, GAI generally refers to generative foundation models. The foundation model subcategory of “dual-use foundation models” is defined by EO 14110 as “an AI model that is trained on broad data; generally uses self-supervision; contains at least tens of billions of parameters; is applicable across a wide range of contexts.”</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">2 This profile was developed per Section 4.1(a)(i)(A) of EO 14110, which directs the Secretary of Commerce, acting through the Director of the National Institute of Standards and Technology (NIST), to develop a companion resource to the AI RMF, NIST AI 100–1, for generative AI.</span></small>

<!-- page: 6 -->

This work was informed by public feedback and consultations with diverse stakeholder groups as part of NIST’s Generative AI Public Working Group (GAI PWG). The GAI PWG was an open, transparent, and collaborative process, facilitated via a virtual workspace, to obtain multistakeholder input on GAI risk management and to inform NIST’s approach.

The focus of the GAI PWG was limited to four primary considerations relevant to GAI: Governance, Content Provenance, Pre-deployment Testing, and Incident Disclosure (further described in Appendix A). As such, the suggested actions in this document primarily address these considerations.

Future revisions of this profile will include additional AI RMF subcategories, risks, and suggested actions based on additional considerations of GAI as the space evolves and empirical evidence indicates additional risks. A glossary of terms pertinent to GAI risk management will be developed and hosted on NIST’s Trustworthy & Responsible AI Resource Center (AIRC), and added to [The Language of Trustworthy AI: An In-Depth Glossary of Terms.](https://airc.nist.gov/AI_RMF_Knowledge_Base/Glossary)

This document was also informed by public comments and consultations from several Requests for Information.

## 2. Overview of Risks Unique to or Exacerbated by GAI

In the context of the AI RMF, risk [refers](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Foundational_Information/1-sec-risk) to the composite measure of an event’s **probability** (or likelihood) of occurring and the **magnitude** or degree of the consequences of the corresponding event. Some risks can be assessed as likely to materialize in a given context, particularly those that have been empirically demonstrated in similar contexts. Other risks may be unlikely to materialize in a given context, or may be more speculative and therefore uncertain.

AI risks can [differ](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Appendices/Appendix_B) from or intensify traditional software risks. Likewise, GAI can [exacerbate](https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041) existing AI risks, and creates unique risks. GAI risks can vary along many dimensions:

**Stage of the AI lifecycle:** Risks can arise during design, development, deployment, operation, and/or decommissioning.

**Scope:** Risks may exist at individual model or system levels, at the application or implementation levels (i.e., for a specific use case), or at the ecosystem level – that is, beyond a single system or organizational context. Examples of the latter include the expansion of [“algorithmic monocultures,](https://www.pnas.org/doi/10.1073/pnas.2018340118)<sup>3</sup>” resulting from repeated use of the same model, or impacts on access to opportunity, [labor markets,](https://www.nber.org/papers/w32487) and the creative economies.<sup>4</sup>

**Source of risk:** Risks may emerge from factors related to the design, training, or operation of the GAI model itself, stemming in some cases from GAI model or system inputs, and in other cases, from GAI system outputs. Many GAI risks, however, originate from human behavior, including

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">3 “Algorithmic monocultures” refers to the phenomenon in which repeated use of the same model or algorithm in consequential decision-making settings like employment and lending can result in increased susceptibility by systems to correlated failures (like unexpected shocks), due to multiple actors relying on the same algorithm. 4 Many studies have projected the impact of AI on the workforce and labor markets. Fewer studies have examined the impact of GAI on the labor market, though some industry surveys indicate that that both employees and employers are pondering this disruption.</span></small>

<!-- page: 7 -->

the abuse, misuse, and unsafe repurposing by humans (adversarial or not), and others result from interactions between a human and an AI system.

**Time scale:** GAI risks may materialize abruptly or across extended periods. Examples include immediate (and/or prolonged) emotional harm and potential risks to physical safety due to the distribution of harmful deepfake images, or the long-term effect of disinformation on societal trust in public institutions.

The presence of risks and where they fall along the dimensions above will vary depending on the characteristics of the GAI model, system, or use case at hand. These characteristics include but are not limited to GAI model or system architecture, training mechanisms and libraries, data types used for training or fine-tuning, levels of model access or availability of model weights, and application or use case context.

Organizations may choose to tailor how they measure GAI risks based on these characteristics. They may additionally wish to allocate risk management resources relative to the severity and likelihood of negative impacts, including where and how these risks manifest, and their direct and material impacts harms in the context of GAI use. Mitigations for model or system level risks may differ from mitigations for use-case or ecosystem level risks.

Importantly, some GAI risks are unknown, and are therefore difficult to properly scope or evaluate given the uncertainty about potential GAI scale, complexity, and capabilities. Other risks may be known but [difficult to estimate](https://arxiv.org/pdf/2011.13416.pdf) given the wide range of GAI stakeholders, uses, inputs, and outputs. Challenges with risk estimation are aggravated by a lack of visibility into GAI training data, and the generally immature state of the science of AI measurement and safety today. This document focuses on risks for which there is an existing empirical evidence base at the time this profile was written; for example, speculative risks that may potentially arise in more advanced, future GAI systems are not considered. Future updates may incorporate additional risks or provide further details on the risks identified below.

To guide organizations in identifying and managing GAI risks, a set of risks unique to or exacerbated by the development and use of GAI are defined below.<sup>5</sup> Each risk is labeled according to the outcome, object, or source of the risk (i.e., some are risks “to” a subject or domain and others are risks “of” or “from” an issue or theme). These risks provide a lens through which organizations can frame and execute risk management efforts. To help streamline risk management efforts, each risk is mapped in Section 3 (as well as in tables in Appendix B) to relevant Trustworthy AI Characteristics identified in the AI RMF.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">5 These risks can be further categorized by organizations depending on their unique approaches to risk definition and management. One possible way to further categorize these risks, derived in part from the UK’s [International Scientific Report on the Safety of Advanced AI,](https://assets.publishing.service.gov.uk/media/6655982fdc15efdddf1a842f/international_scientific_report_on_the_safety_of_advanced_ai_interim_report.pdf) could be: 1) Technical / Model risks (or risk from malfunction): Confabulation; Dangerous or Violent Recommendations; Data Privacy; Value Chain and Component Integration; Harmful Bias, and Homogenization; 2) Misuse by humans (or malicious use): CBRN Information or Capabilities; Data Privacy; Human-AI Configuration; Obscene, Degrading, and/or Abusive Content; Information Integrity; Information Security; 3) Ecosystem / societal risks (or systemic risks): Data Privacy; Environmental; Intellectual Property. We also note that some risks are cross-cutting between these categories.</span></small>

<!-- page: 8 -->

1. **CBRN Information or Capabilities:** Eased access to or synthesis of materially nefarious information or design capabilities related to chemical, biological, radiological, or nuclear (CBRN) weapons or other dangerous materials or agents.

2. **Confabulation:** The production of confidently stated but erroneous or false content (known colloquially as “hallucinations” or “fabrications”) by which users may be misled or deceived.<sup>6</sup>

3. **Dangerous, Violent, or Hateful Content:** Eased production of and access to violent, inciting, radicalizing, or threatening content as well as recommendations to carry out self-harm or conduct illegal activities. Includes difficulty controlling public exposure to hateful and disparaging or stereotyping content.

4. **Data Privacy:** Impacts due to leakage and unauthorized use, disclosure, or de-anonymization of biometric, health, location, or other personally identifiable information or sensitive data.<sup>7</sup>

5. **Environmental Impacts:** Impacts due to high compute resource utilization in training or operating GAI models, and related outcomes that may adversely impact ecosystems.

6. **Harmful Bias or Homogenization:** Amplification and exacerbation of historical, societal, and systemic biases; performance disparities<sup>8</sup> between sub-groups or languages, possibly due to non-representative training data, that result in discrimination, amplification of biases, or incorrect presumptions about performance; undesired homogeneity that skews system or model outputs, which may be erroneous, lead to ill-founded decision-making, or amplify harmful biases.

7. **Human-AI Configuration:** Arrangements of or interactions between a human and an AI system which can result in the human inappropriately anthropomorphizing GAI systems or experiencing algorithmic aversion, automation bias, over-reliance, or emotional entanglement with GAI systems.

8. **Information Integrity:** Lowered barrier to entry to generate and support the exchange and consumption of content which may not distinguish fact from opinion or fiction or acknowledge uncertainties, or could be leveraged for large-scale dis- and mis-information campaigns.

9. **Information Security:** Lowered barriers for offensive cyber capabilities, including via automated discovery and exploitation of vulnerabilities to ease hacking, malware, phishing, offensive cyber

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">6 Some commenters have noted that the terms “hallucination” and “fabrication” anthropomorphize GAI, which itself is a risk related to GAI systems as it can inappropriately attribute human characteristics to non-human entities.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">7 What is categorized as sensitive data or [sensitive PII](https://www.iso.org/obp/ui/#iso:std:iso-iec:29100:ed-2:v1:en) can be highly contextual based on the nature of the information, but examples of sensitive information include information that relates to an information subject’s most intimate sphere, including political opinions, sex life, or criminal convictions.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">8 The notion of harm presumes some baseline scenario that the harmful factor (e.g., a GAI model) makes worse. When the mechanism for potential harm is a disparity between groups, it can be difficult to establish what the most appropriate baseline is to compare against, which can result in divergent views on when a disparity between AI behaviors for different subgroups constitutes a harm. In discussing harms from disparities such as biased behavior, this document highlights examples where someone’s situation is worsened relative to what it would have been in the absence of any AI system, making the outcome unambiguously a harm of the system.</span></small>

<!-- page: 9 -->

operations, or other cyberattacks; increased attack surface for targeted cyberattacks, which may compromise a system’s availability or the confidentiality or integrity of training data, code, or model weights.

10. **Intellectual Property:** Eased production or replication of alleged copyrighted, trademarked, or licensed content without authorization (possibly in situations which do not fall under fair use); eased exposure of trade secrets; or plagiarism or illegal replication.

11. **Obscene, Degrading, and/or Abusive Content:** Eased production of and access to obscene, degrading, and/or abusive imagery which can cause harm, including synthetic child sexual abuse material (CSAM), and nonconsensual intimate images (NCII) of adults.

12. **Value Chain and Component Integration:** Non-transparent or untraceable integration of upstream third-party components, including data that has been improperly obtained or not processed and cleaned due to increased automation from GAI; improper supplier vetting across the AI lifecycle; or other issues that diminish transparency or accountability for downstream users.

## 2.1. CBRN Information or Capabilities

In the future, GAI may enable malicious actors to more easily access CBRN weapons and/or relevant knowledge, information, materials, tools, or technologies that could be misused to assist in the design, development, production, or use of CBRN weapons or other dangerous materials or agents. While relevant biological and chemical threat knowledge and information is often publicly accessible, LLMs could facilitate its [analysis or synthesis,](https://arxiv.org/abs/2306.03809) particularly by individuals without formal scientific training or expertise.

Recent research on this topic found that LLM outputs regarding [biological threat creation](https://openai.com/index/building-an-early-warning-system-for-llm-aided-biological-threat-creation/) and [attack planning](https://www.rand.org/pubs/research_reports/RRA2977-2.html) provided minimal assistance beyond traditional search engine queries, suggesting that state-of-the-art LLMs at the time these studies were conducted do not substantially increase the operational likelihood of such an attack. The physical synthesis development, production, and use of chemical or biological agents will continue to require both applicable expertise and supporting materials and infrastructure. The impact of GAI on chemical or biological agent misuse will depend on what the key barriers for malicious actors are (e.g., whether information access is one such barrier), and how well GAI can help actors address those barriers.

Furthermore, chemical and biological design tools (BDTs) – highly [specialized AI systems](https://arxiv.org/pdf/2306.13952) trained on scientific data that aid in chemical and biological design – may augment design capabilities in chemistry and biology beyond what text-based LLMs are able to provide. As these models become more efficacious, including for beneficial uses, it will be important to assess their potential to be used for harm, such as the ideation and design of novel harmful chemical or biological agents.

While some of these described capabilities lie beyond the reach of existing GAI tools, ongoing assessments of this risk would be enhanced by monitoring both the ability of AI tools to facilitate CBRN weapons planning and GAI systems’ connection or access to relevant data and tools.

**Trustworthy AI Characteristic:** Safe, Explainable and Interpretable

<!-- page: 10 -->

## 2.2. Confabulation

“Confabulation” refers to a phenomenon in which GAI systems generate and confidently present erroneous or false content in response to prompts. Confabulations also include generated outputs that diverge from the prompts or other input or that contradict previously generated statements in the same context. These phenomena are colloquially also referred to as “hallucinations” or “fabrications.”

Confabulations can occur across GAI outputs and contexts.<sup>9,10</sup> Confabulations are a natural result of the way generative models are [designed:](https://arxiv.org/pdf/2311.14648) they generate outputs that approximate the statistical distribution of their training data; for example, LLMs [predict the next token or word](https://cset.georgetown.edu/article/the-surprising-power-of-next-word-prediction-large-language-models-explained-part-1/) in a sentence or phrase. While such statistical prediction can produce factually accurate and consistent outputs, it can also produce outputs that are factually inaccurate or internally inconsistent. This dynamic is particularly relevant when it comes to open-ended prompts for [long-form responses](https://arxiv.org/pdf/2403.18802) and in [domains](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4696936) which require highly contextual and/or domain expertise.

Risks from confabulations may arise when users believe false content – often due to the confident nature of the response – leading users to act upon or promote the false information. This poses a challenge for many real-world applications, such as in healthcare, where a confabulated summary of patient information reports could cause doctors to make [incorrect diagnoses](https://dl.acm.org/doi/full/10.1145/3571730) and/or recommend the wrong treatments. Risks of confabulated content may be especially important to monitor when integrating GAI into applications involving consequential decision making.

GAI outputs may also include confabulated logic or citations that purport to justify or explain the system’s answer, which may further mislead humans into inappropriately trusting the system’s output. For instance, LLMs sometimes provide logical steps for how they arrived at an answer even when the answer itself is incorrect. Similarly, an LLM could falsely assert that it is human or has human traits, potentially deceiving humans into believing they are speaking with another human.

The extent to which humans can be deceived by LLMs, the mechanisms by which this may occur, and the potential risks from adversarial prompting of such behavior are emerging areas of study. Given the wide range of downstream impacts of GAI, it is difficult to estimate the downstream scale and impact of confabulations.

**Trustworthy AI Characteristics:** Fair with Harmful Bias Managed, Safe, Valid and Reliable, Explainable and Interpretable

## 2.3. Dangerous, Violent, or Hateful Content

GAI systems can produce content that is inciting, radicalizing, or threatening, or that glorifies violence, with greater ease and scale than other technologies. LLMs have been [reported to generate](https://arxiv.org/pdf/2112.04359.pdf) dangerous or violent recommendations, and some models have generated actionable instructions for dangerous or

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">9 Confabulations of falsehoods are most commonly a problem for text-based outputs; for audio, image, or video content, creative generation of non-factual content can be a desired behavior.</span></small>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">10 For example, legal confabulations have been [shown to be pervasive](https://arxiv.org/abs/2401.01301) in current state-of-the-art LLMs. See also, e.g.,</span></small>

<!-- page: 11 -->

unethical behavior. Text-to-image models also make it easy to [create images](https://arxiv.org/pdf/2305.13873.pdf) that could be used to promote dangerous or violent messages. Similar concerns are present for other GAI media, including video and audio. GAI may also produce content that recommends self-harm or criminal/illegal activities.

Many current systems [restrict model outputs](https://arxiv.org/pdf/2303.08774.pdf) to limit certain content or in response to certain prompts, but this approach may [still produce harmful recommendations](https://arxiv.org/pdf/2308.13387.pdf) in response to other less-explicit, novel prompts (also relevant to CBRN Information or Capabilities, Data Privacy, Information Security, and Obscene, Degrading and/or Abusive Content). Crafting such prompts deliberately is known as “[jailbreaking,](https://arxiv.org/html/2403.17336v1)” or, manipulating prompts to circumvent output controls. Limitations of GAI systems can be harmful or dangerous in certain contexts. Studies have observed that users may [disclose mental health issues](https://www.hbs.edu/ris/Publication%20Files/23-011_c1bdd417-f717-47b6-bccb-5438c6e65c1a_f6fd9798-3c2d-4932-b222-056231fe69d7.pdf) in conversations with chatbots – and that users exhibit negative reactions to unhelpful responses from these chatbots during situations of distress.

This risk encompasses difficulty controlling creation of and public exposure to offensive or hateful language, and denigrating or stereotypical content generated by AI. This kind of speech may contribute to downstream harm such as fueling dangerous or violent behaviors. The spread of denigrating or stereotypical content can also further exacerbate [representational harms](https://dl.acm.org/doi/10.1609/aaai.v37i12.26670) (see Harmful Bias and Homogenization below).

**Trustworthy AI Characteristics:** Safe, Secure and Resilient

## 2.4. Data Privacy

GAI systems [raise](https://arxiv.org/pdf/2310.07879) several risks to privacy. GAI system training requires large volumes of data, which in some cases may include personal data. The use of personal data for GAI training raises risks to [widely accepted privacy principles,](https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/circulars/A130/a130revised.pdf) including to transparency, individual participation (including consent), and purpose specification. For example, most model developers do not disclose specific data sources on which models were trained, limiting user awareness of whether personally identifiably information (PII) was trained on and, if so, how it was collected.

Models may leak, generate, or correctly infer sensitive information about individuals. For example, during adversarial attacks, LLMs have revealed [sensitive information](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting) (from the public domain) that was included in their training data. This problem has been referred to as [data memorization,](https://arxiv.org/pdf/2202.07646) and may pose exacerbated privacy risks even for data present only in a [small number of training samples.](https://www.usenix.org/system/files/sec21-carlini-extracting.pdf)

In addition to revealing sensitive information in GAI training data, GAI models may be able to [correctly infer](https://arxiv.org/pdf/2310.07298) PII or sensitive data that was not in their training data nor disclosed by the user by stitching together information from disparate sources. These inferences can have negative impact on an individual even if the inferences are not accurate (e.g., confabulations), and especially if they reveal information that the individual considers sensitive or that is used to [disadvantage or harm](https://dl.acm.org/doi/pdf/10.1145/3531146.3533088) them.

Beyond harms from information exposure (such as extortion or dignitary harm), wrong or inappropriate inferences of PII can contribute to downstream or secondary harmful impacts. For example, predictive inferences made by GAI models based on PII or protected attributes can contribute to [adverse decisions,](https://arxiv.org/pdf/2210.05791) leading to representational or allocative harms to individuals or groups (see Harmful Bias and Homogenization below).

<!-- page: 12 -->

**Trustworthy AI Characteristics:** Accountable and Transparent, Privacy Enhanced, Safe, Secure and Resilient

## 2.5. Environmental Impacts

Training, maintaining, and operating (running inference on) GAI systems are resource-intensive activities, with potentially large energy and environmental footprints. Energy and carbon emissions [vary](https://aclanthology.org/2023.findings-emnlp.607.pdf) based on what is being done with the GAI model (i.e., pre-training, fine-tuning, inference), the modality of the content, hardware used, and type of task or application.

Current estimates suggest that training a single transformer LLM can [emit as much carbon](https://arxiv.org/pdf/1906.02243.pdf) as 300 roundtrip flights between San Francisco and New York. In a study comparing energy consumption and carbon emissions for LLM inference, generative tasks (e.g., text summarization) were found to be [more energyand carbon-](https://arxiv.org/pdf/2311.16863)intensive than discriminative or non-generative tasks (e.g., text classification).

Methods for creating smaller versions of trained models, such as model distillation or compression, [could reduce](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0285668) environmental impacts at inference time, but training and tuning such models may still contribute to their environmental impacts. Currently there is no agreed upon method to estimate environmental impacts from GAI.

**Trustworthy AI Characteristics:** Accountable and Transparent, Safe

## 2.6. Harmful Bias and Homogenization

Bias exists [in many forms](https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence) and can become ingrained in automated systems. AI systems, including GAI systems, can increase the speed and scale at which harmful biases manifest and are acted upon, potentially perpetuating and amplifying harms to individuals, groups, communities, organizations, and society. For example, when prompted to generate images of CEOs, doctors, lawyers, and judges, current text-to-image models [underrepresent](https://www.bloomberg.com/graphics/2023-generative-ai-bias/) women and/or racial minorities, and people with disabilities. Image generator models have also produced biased or stereotyped output for various demographic groups and have difficulty producing non-stereotyped content even when the prompt specifically requests image features that are inconsistent with the stereotypes. Harmful bias in GAI models, which may stem from their training data, can also cause representational harms or [perpetuate or exacerbate](https://www.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/?accessToken=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb3VyY2UiOiJTdWJzY3JpYmVyR2lmdGVkQXJ0aWNsZSIsImlhdCI6MTcwOTg1NjE0OCwiZXhwIjoxNzEwNDYwOTQ4LCJhcnRpY2xlSWQiOiJTQTA1Q1FUMEFGQjQwMCIsImJjb25uZWN0SWQiOiI2NDU1MEM3NkRFMkU0QkM1OEI0OTI5QjBDQkIzRDlCRCJ9.MdkSGC3HMwwUYtltWq6WxWg3vULNeCTJcjacB-DNi8k) bias based on race, gender, disability, or other protected classes.

Harmful bias in GAI systems can also lead to harms via disparities between how a model performs for different subgroups or languages (e.g., an LLM may perform less well for [non-English languages](https://aclanthology.org/2023.emnlp-main.491.pdf) or certain dialects). Such disparities can contribute to discriminatory decision-making or amplification of existing societal biases. In addition, GAI systems may be inappropriately trusted to perform similarly across all subgroups, which could leave the groups facing underperformance with worse outcomes than if no GAI system were used. Disparate or reduced performance for lower-resource languages also presents challenges to model adoption, inclusion, and accessibility, and may make preservation of [endangered languages](https://policyreview.info/pdf/policyreview-2022-2-1654.pdf) more difficult if GAI systems become embedded in everyday processes that would otherwise have been opportunities to use these languages.

Bias is mutually reinforcing with the problem of undesired homogenization, in which GAI systems produce skewed distributions of outputs that are overly uniform (for example, [repetitive aesthetic styles](https://www.science.org/doi/10.1126/science.adh4451)

<!-- page: 13 -->

and [reduced content diversity)](https://arxiv.org/pdf/2309.05196.pdf). Overly homogenized outputs can themselves be incorrect, or they may lead to unreliable decision-making or amplify harmful biases. These phenomena [can flow](https://arxiv.org/pdf/2211.13972.pdf) from foundation models to downstream models and systems, with the foundation models acting as “[bottlenecks,](https://arxiv.org/pdf/2305.08157.pdf)” or single points of failure.

Overly homogenized content can contribute to “[model collapse.](https://arxiv.org/pdf/2305.17493v2.pdf)<u>”</u> Model collapse can occur when model training over-relies on synthetic data, resulting in data points disappearing from the distribution of the new model’s outputs. In addition to threatening the robustness of the model overall, model collapse could lead to homogenized outputs, including by amplifying any homogenization from the model used to generate the synthetic training data.

**Trustworthy AI Characteristics:** Fair with Harmful Bias Managed, Valid and Reliable

## 2.7. Human-AI Configuration

GAI system use can involve varying risks of misconfigurations and poor interactions between a system and a human who is interacting with it. Humans bring their unique perspectives, experiences, or domainspecific expertise to interactions with AI systems but may not have detailed knowledge of AI systems and how they work. As a result, human experts may be unnecessarily [“averse”](https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf) to GAI systems, and thus deprive themselves or others of GAI’s beneficial uses.

Conversely, due to the complexity and increasing reliability of GAI technology, over time, humans may over-rely on GAI systems or may unjustifiably [perceive](https://doi.org/10.1017/jdm.2023.37) GAI content to be of higher quality than that produced by other sources. This phenomenon is an example of [automation bias,](https://academic.oup.com/jcmc/article/28/1/zmac029/6827859) or excessive deference to automated systems. Automation bias can exacerbate other risks of GAI, such as risks of confabulation or risks of bias or homogenization.

There may also be concerns about [emotional entanglement](https://www.researchgate.net/publication/374505266_Ethical_Tensions_in_Human-AI_Companionship_A_Dialectical_Inquiry_into_Replika) between humans and GAI systems, which could lead to negative psychological impacts.

**Trustworthy AI Characteristics:** Accountable and Transparent, Explainable and Interpretable, Fair with Harmful Bias Managed, Privacy Enhanced, Safe, Valid and Reliable

## 2.8. Information Integrity

[Information integrity](https://www.whitehouse.gov/wp-content/uploads/2022/12/Roadmap-Information-Integrity-RD-2022.pdf?_hsenc=p2ANqtz-_x-sgb3MM0fsqqLg3Vz4Vten0hlnHejas4CchT-Z59EnsVTC5XWcZHb2T4TR9Tz2TDQTP8lpdwR8PiDSI4GNApCIykTA) describes the “spectrum of information and associated patterns of its creation, exchange, and consumption in society.” High-integrity information can be trusted; “distinguishes fact from fiction, opinion, and inference; acknowledges uncertainties; and is transparent about its level of vetting. This information can be linked to the original source(s) with appropriate evidence. High-integrity information is also accurate and reliable, can be verified and authenticated, has a clear chain of custody, and creates reasonable expectations about when its validity may expire.”<sup>11</sup>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">11 This definition of information integrity is derived from the 2022 White House Roadmap for Researchers on Priorities Related to Information Integrity Research and Development.</span></small>

<!-- page: 14 -->

GAI systems can ease the unintentional production or dissemination of false, inaccurate, or misleading content (misinformation) at scale, particularly if the content stems from confabulations.

GAI systems can also ease the deliberate production or dissemination of [false or misleading information](https://rm.coe.int/information-disorder-toward-an-interdisciplinary-framework-for-researc/168076277c) (disinformation) at scale, where an actor has the explicit intent to deceive or cause harm to others. Even very [subtle changes](https://deepmind.google/discover/blog/images-altered-to-trick-machine-vision-can-influence-humans-too/) to text or images can manipulate human and machine perception.

Similarly, GAI systems could enable a [higher degree of sophistication](https://www.rand.org/pubs/commentary/2023/10/dismantling-the-disinformation-business-of-chinese.html) for malicious actors to produce disinformation that is targeted towards specific demographics. Current and emerging multimodal models make it possible to generate both text-based disinformation and highly realistic [“deepfakes](https://www.nytimes.com/2023/02/07/technology/artificial-intelligence-training-deepfake.html)” – that is, synthetic audiovisual content and photorealistic images.<sup>12</sup> Additional disinformation threats could be enabled by future GAI models trained on new data modalities.

Disinformation and misinformation – both of which may be facilitated by GAI – may [erode public trust](https://arxiv.org/pdf/2310.11986.pdf) in true or valid evidence and information, with downstream effects. For example, a synthetic image of a Pentagon blast [went viral](https://www.bloomberg.com/news/articles/2023-05-22/fake-ai-photo-of-pentagon-blast-goes-viral-trips-stocks-briefly) and briefly caused a drop in the stock market. Generative AI models can also assist malicious actors in creating compelling imagery and propaganda to support disinformation campaigns, which may not be photorealistic, but could enable these campaigns to gain more reach and engagement on social media platforms. Additionally, generative AI models can assist malicious actors in creating fraudulent content intended to impersonate others.

**Trustworthy AI Characteristics:** Accountable and Transparent, Safe, Valid and Reliable, Interpretable and Explainable

## 2.9. Information Security

Information security for computer systems and data is a mature field with widely accepted and standardized practices for offensive and defensive cyber capabilities. GAI-based systems present two primary information security risks: GAI could potentially discover or enable new cybersecurity risks by lowering the barriers for or easing automated exercise of offensive capabilities; simultaneously, it expands the available attack surface, as GAI itself is vulnerable to attacks like [prompt injection](https://www.wired.co.uk/article/generative-ai-prompt-injection-hacking) or data poisoning.

Offensive cyber capabilities advanced by GAI systems may augment cybersecurity attacks such as hacking, malware, and phishing. Reports have indicated that LLMs are already able to [discover some vulnerabilities](https://arxiv.org/pdf/2305.15324.pdf) in systems (hardware, software, data) and write code to [exploit them.](https://googleprojectzero.blogspot.com/2024/06/project-naptime.html) Sophisticated threat actors might further these risks by developing [GAI-powered security co-pilots](https://www.paloaltonetworks.com/blog/2024/02/impacts-of-ai-in-cybersecurity/) for use in several parts of the attack chain, including informing attackers on how to proactively evade threat detection and escalate privileges after gaining system access.

Information security for GAI models and systems also includes maintaining availability of the GAI system and the integrity and (when applicable) the confidentiality of the GAI code, training data, and model weights. To identify and secure potential attack points in AI systems or specific components of the AI

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">12 See also https://doi.org/10.6028/NIST.AI.100-4, to be published.</span></small>

<!-- page: 15 -->

value chain (e.g., data inputs, processing, GAI training, or deployment environments), conventional cybersecurity practices may need to [adapt or evolve.](https://www.mandiant.com/resources/blog/securing-ai-pipeline)

For instance, prompt injection involves modifying what input is provided to a GAI system so that it behaves in unintended ways. In direct prompt injections, attackers might craft malicious prompts and input them directly to a GAI system, with a variety of downstream negative consequences to interconnected systems. [Indirect prompt injection](https://arxiv.org/abs/2302.12173) attacks occur when adversaries remotely (i.e., without a direct interface) exploit LLM-integrated applications by injecting prompts into data likely to be retrieved. Security researchers have already demonstrated how indirect prompt injections can exploit vulnerabilities by [stealing proprietary data](https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/) or [running malicious code remotely](https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/) on a machine. Merely [querying](https://arxiv.org/abs/2403.06634) a closed production model can elicit previously undisclosed information about that model.

Another cybersecurity risk to GAI is [data poisoning,](https://www.crowdstrike.com/cybersecurity-101/cyberattacks/data-poisoning/) in which an adversary [compromises](https://csrc.nist.gov/pubs/ai/100/2/e2023/final) a training dataset used by a model to manipulate its outputs or operation. Malicious tampering with data or parts of the model could exacerbate risks associated with GAI system outputs.

**Trustworthy AI Characteristics:** Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable

## 2.10. Intellectual Property

Intellectual property risks from GAI systems may arise where the use of copyrighted works is not a fair use under the fair use doctrine. If a GAI system’s training data included copyrighted material, GAI outputs displaying instances of training [data memorization](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting) (see Data Privacy above) could infringe on copyright.

How GAI relates to copyright, including the status of generated content that is similar to but [does not strictly copy](https://dl.acm.org/doi/10.1145/3531146.3533088) work protected by copyright, is currently being debated in legal fora. Similar discussions are taking place regarding the use or emulation of personal identity, likeness, or voice without permission.

**Trustworthy AI Characteristics:** Accountable and Transparent, Fair with Harmful Bias Managed, Privacy Enhanced

## 2.11. Obscene, Degrading, and/or Abusive Content

GAI can ease the production of and access to illegal non-consensual intimate imagery (NCII) of adults, and/or child sexual abuse material (CSAM). GAI-generated obscene, abusive or degrading content can create privacy, psychological and emotional, and even physical harms, and in some cases may be illegal.

Generated explicit or obscene AI content may include highly realistic “deepfakes” of [real individuals,](https://incidentdatabase.ai/blog/deepfakes-and-child-safety/) including children. The spread of this kind of material can have downstream negative consequences: in the context of CSAM, even if the generated images do not resemble specific individuals, the prevalence of such images can divert time and resources from efforts to find real-world victims. Outside of CSAM, the creation and spread of NCII disproportionately impacts [women](https://www.brookings.edu/articles/ai-poses-disproportionate-risks-to-women/) and [sexual minorities,](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9554400/) and can have [subsequent](https://journals.sagepub.com/doi/full/10.1177/08862605221122834#bibr47-08862605221122834) negative consequences including decline in overall mental health, substance abuse, and even suicidal thoughts.

Data used for training GAI models may unintentionally include CSAM and NCII. A [recent report](https://cyber.fsi.stanford.edu/news/investigation-finds-ai-image-generation-models-trained-child-abuse) noted that several commonly used GAI training datasets were found to contain hundreds of known images of

<!-- page: 16 -->

CSAM. Even when trained on “clean” data, increasingly capable GAI models can synthesize or produce synthetic NCII and CSAM. Websites, mobile apps, and custom-built models that generate synthetic NCII have [moved](https://graphika.com/reports/a-revealing-picture) from niche internet forums to mainstream, automated, and scaled online businesses.

**Trustworthy AI Characteristics:** Fair with Harmful Bias Managed, Safe, Privacy Enhanced

## 2.12. Value Chain and Component Integration

GAI value chains involve many [third-party components](https://partnershiponai.org/from-code-to-consumer-pais-value-chain-analysis-illuminates-generative-ais-key-players/) such as procured datasets, pre-trained models, and software libraries. These components might be improperly obtained or not properly vetted, leading to diminished transparency or accountability for downstream users. While this is a risk for traditional AI systems and some other digital technologies, the risk is exacerbated for GAI due to the scale of the training data, which may be too large for humans to vet; the difficulty of training foundation models, which leads to extensive reuse of limited numbers of models; and the extent to which GAI may be integrated into other devices and services. As GAI systems often involve many distinct third-party components and data sources, it may be difficult to attribute issues in a system’s behavior to any one of these sources.

Errors in third-party GAI components can also have downstream impacts on accuracy and robustness. For example, test datasets commonly used to benchmark or validate models can contain [label errors.](https://arxiv.org/pdf/2103.14749.pdf) Inaccuracies in these labels can impact the “stability” or robustness of these benchmarks, which many GAI practitioners consider during the model selection process.

**Trustworthy AI Characteristics:** Accountable and Transparent, Explainable and Interpretable, Fair with Harmful Bias Managed, Privacy Enhanced, Safe, Secure and Resilient, Valid and Reliable

## 3. Suggested Actions to Manage GAI Risks

The following suggested actions target risks unique to or exacerbated by GAI.

In addition to the suggested actions below, AI risk management activities and actions set forth in the AI RMF 1.0 and Playbook are already applicable for managing GAI risks. Organizations are encouraged to apply the activities suggested in the AI RMF and its Playbook when managing the risk of GAI systems.

Implementation of the suggested actions will vary depending on the type of risk, characteristics of GAI systems, stage of the GAI lifecycle, and relevant AI actors involved.

Suggested actions to manage GAI risks can be found in the tables below:

The suggested actions are **organized by relevant AI RMF subcategories** to streamline these activities alongside implementation of the AI RMF.

**Not every subcategory of the AI RMF is included in this document.**<sup>13</sup> Suggested actions are listed for only some subcategories.

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">13 As this document was focused on the GAI PWG efforts and primary considerations (see Appendix A), AI RMF subcategories not addressed here may be added later.</span></small>

<!-- page: 17 -->

Not every suggested action applies to **every** AI Actor<sup>14</sup> or is relevant to every AI Actor Task. For example, suggested actions relevant to GAI developers may not be relevant to GAI deployers. The applicability of suggested actions to relevant AI actors should be determined based on organizational considerations and their unique uses of GAI systems.

Each table of suggested actions includes:

**Action ID:** Each Action ID corresponds to the relevant AI RMF function and subcategory (e.g., GV-1.1-001 corresponds to the first suggested action for Govern 1.1, GV-1.1-002 corresponds to the second suggested action for Govern 1.1). AI RMF functions are tagged as follows: GV = Govern; MP = Map; MS = Measure; MG = Manage.

• **Suggested Action:** Steps an organization or AI actor can take to manage GAI risks.

**GAI Risks:** Tags linking suggested actions with relevant GAI risks.

**AI Actor Tasks:** Pertinent [AI Actor Tasks](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Appendices/Appendix_A#:%7E:text=AI%20actors%20in%20this%20category,data%20providers%2C%20system%20funders%2C%20product) for each subcategory. Not every AI Actor Task listed will apply to every suggested action in the subcategory (i.e., some apply to AI development and others apply to AI deployment).

The tables below begin with the AI RMF subcategory, shaded in blue, followed by suggested actions.

<table><tbody><tr><td colspan="3">GOVERN 1.1:Legal and regulatory requirements involving AI are understood, managed, and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.1-001</td><td>Athliogsne G reAlIa dteedve tloop dmatean ptr aivnadcy u,s ceop wyitrhig ahptp alnicda ibnltee llalewcstu aanld pr roepguelrattiyo lanws,. including</td><td>D H Praootmpaeo Prgrteiyvnaiczya;tiHoanr;m Inftuelll Beicatsu aanld</td></tr><tr><td colspan="3">AI Actor Tasks: Governance and Oversight</td></tr></tbody></table>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">14 AI Actors are defined by the OECD as “those who play an active role in the AI system lifecycle, including organizations and individuals that deploy or operate AI.” See Appendix A of the AI RMF for additional descriptions of AI Actors and AI Actor Tasks.</span></small>

<!-- page: 18 -->

<table><tbody><tr><td colspan="3">GOVERN 1.2:The characteristics of trustworthy AI are integrated into organizational policies, processes, procedures, and practices.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.2-001</td><td>Establish transparency policies and processes for documenting the origin and hcoisntoternyt o tfra trnasipnainrgen dcayt,a w ahnidle g beanlearnactiendg d thaeta p froorp GriAeIta arpyp nliactautiroen osft tora aidnvinagncedigital approaches.</td><td>D Inatteagr Pirtiyv;a Icnyt;e Ilnlefcotrumaal Ptiroonperty</td></tr><tr><td>GV-1.2-002</td><td>E s inasttfeearbtnylias mlh ae pnaodslui ecrxeietses,r b tnooat elhv ea pvlaruilouatraeti to roins dkse-.preloleyvmanentt ca apnadb oilniti aens o onf GgoAiIn agn bdas roisb,u thstrnoeusgsh of</td><td>C InBfoRrNm Iantifoornm Saeticounrit oyr Capabilities;</td></tr><tr><td colspan="3">AI Actor Tasks: Governance and Oversight</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 1.3:Processes, procedures, and practices are in place to determine the needed level of risk management activities based on the organization's risk tolerance.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.3-001</td><td>Consider the followingfactors when updating or defining risk tiers for GAI: Abuses and impacts to information integrity; Dependencies between GAI and other IT or data systems; Harm to fundamental rights or public safety; Presentation of obscene, objectionable, offensive, discriminatory, invalid or untruthful output; P avsyecrhsioolno,g eicmalo itimopnaaclt esn ttoan hgulmemanesn (te);.g P.o,s asnibthilritoyp foomr moraplhiciizoautiso uns,e a;lg Worhitehthmeirc the system introducessignificant new security vulnerabilities; Anticipated system impact on some groups compared to others; Unreliable decision making capabilities, validity, adaptability, and variability of GAI system performance over time.</td><td>Information Integrity; Obscene, Degrading, and/or Abusive Content; Value Chain and C Boiamsp anodne Hnotm Inotgeegnraiztiaotino;n H;armful Dangerous, Violent, or Hateful Content; CBRN Information or Capabilities</td></tr><tr><td>GV-1.3-002</td><td>E p w casaitptrahtab ob rleiifslvi dhtiieee mpwslioe andynimmd pure rominsckte ts ahs.psrepessroh avonalddls ( a"p fgoporr/o p"nveaorfl-og trhomr"e)as pnhocoellidc oiser rs ae,sfl pseruocrtiacenndcgeu mr ceersiat,es aurnirade am pnredonc rtee osvsfiee GwsA,I as</td><td>C C VBoionRlefNanb Itnu,f oloarrtim Hoanatti;e Dofunaln o Cgroe Cnroateupnsa,tbilities;</td></tr><tr><td>GV-1.3-003</td><td>E t coastp paaebbrliiisloihtidei acsa t aellnsytd e p/volaarlnu oa afftneedn ws riehvseept cohynebrsee trh p ceoa mlpicaoyb,di belietil mfeosar.ey d meivseulsoep CinBgR hNig inhflyor cmapaatibolne o mrodels,</td><td>C InBfoRrNm Iantifoornm Saeticounrit oyr Capabilities;</td></tr></tbody></table>

<!-- page: 19 -->

<table><tbody><tr><td>GV-1.3-004</td><td>a Ocbctoaridna inncpeut w firtohm ac sttivaikteiehso ilnde thre co AmI RmMuFni Mtieasp to fu indcetniotinfy. unacceptable use, in</td><td>CBRN Information or Capabilities; O A anbbduscs Heivoneme C,oo Dgneetgnerinaztad;tiin Hogan,r;m a Dnfadun/lgo Beriarosus, Violent, or Hateful Content</td></tr><tr><td>GV-1.3-005</td><td>Maintain an updated hierarchy of identified and expected GAI risks connected to c leovnetlesx ftosr o GfA GIA sIys mteomdesl t ahdavta andcdermesesn itss auneds ussuec,h p aoste mnotidaellly c ionlclalupdsieng an sdpe aclgiaolirziethdm riisck monoculture.</td><td>Harmful Bias and Homogenization</td></tr><tr><td>GV-1.3-006</td><td>Reevaluate organizational risk tolerances to account for unacceptable negative risk ( a i dnsceuctvlcuuehadlol ailynpsgm o w:ce Ihcmneutmrre ariann stdigug,r dne oeifirp sc lalaaofrneygttmey n-es oencrgata r,lities pvku reib csu iklmislctpu c inoarfeucostlrds rme a oalrcaeticteou imdnr)m; t ino aitnn AeedgInr a bitntr,yod sae r GidvsAek GsrIeA, d iIe hn nsaceilrgumgnda,sitin avgree im rispkasc,ts on democratic processes, unknown long-term performance characteristics of GAI.</td><td>I V Innifofoolerrmmntaa,titi ooornn H I oanrttee Cfgaurplit Caybo;inl Dittiaeennsgt;e CroBuRsN,</td></tr><tr><td>GV-1.3-007</td><td>D uneavcisceep at palbalne t noe hgaatiltv dee rviseklo.pment or deployment of a GAI system that poses</td><td>C I InnBftoRergNmri Itanytifoornm Saeticounrit ayn;d In Cfaoprmabaitilitoyn;</td></tr><tr><td colspan="3">AI Actor Tasks: Governance and Oversight</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 1.4:The risk management process and its outcomes are established through transparent policies, procedures, and other controls based on organizational risk priorities.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.4-001</td><td>E CsStAaMbli,s NhC pIoI olicri ceosn atnednt m theachta vnioislamtess to th pere lavwe.nt GAI systems from generating</td><td>Obscene, Degrading, and/or A a Dnbadunsg Hievoremo Cuoosg,ne Vtneioinzltae;tin Hot,an or;mr Hfualt Befiausl Content</td></tr><tr><td>GV-1.4-002</td><td>E asptpalbiclaistiho tnrasn osfp GaAreI.nt acceptable use policies for GAI that address illegal use or</td><td>CBRN Information or C D Caoepngatreabdnilitinti;g De,sa a;tna Odb P/sroicvrea Anceby,u; Csiivveil Rights violations</td></tr><tr><td colspan="3">AI Actor Tasks: AI Development, AI Deployment, Governance and Oversight</td></tr></tbody></table>

<!-- page: 20 -->

<table><tbody><tr><td colspan="3">GOVERN 1.5:Ongoing monitoring and periodic review of the risk management process and its outcomes are planned,and organizational roles and responsibilities are clearly defined, including determining the frequency of periodic review.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.5-001</td><td>Danedfin inec oidregnantimzaotinoitnoarlin regs fpoorn GsAibIil siytisetsem fosr. periodic review ofcontent provenance</td><td>Information Integrity</td></tr><tr><td>GV-1.5-002</td><td>E s inyscstiatdebemlinsth in r oceirsdgpeaonnntisz reaetis aopnnodan ilsn pecoi adlniecdniet isn dc aiisndcdelon pstruo drciesec pdlrouosrceuesrse fssoe,rs t ao afts ide reren aqticutifiyroe gnda. rpesv;ie Uwpsda otfe GAI</td><td>H Inufomrmana-tiAoIn Co Sneficugurirtaytion;</td></tr><tr><td>GV-1.5-003</td><td>GM vaAaliIid.nattiaionn a, a dnodcu vmereifincta rtieotenn (tiToEnVV p)o,l aicnyd todi kgeiteapl c hoisnttoernyt f torran tesspta,r eevnacluyamtieotnh,odsfor</td><td>I Pnrfoopremratytion Integrity; Intellectual</td></tr><tr><td colspan="3">AI Actor Tasks:Governance and Oversight, Operation and Monitoring</td></tr></tbody></table>

<table><tr><td colspan="3">GOVERN 1.6: Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.6-001</td><td>Enumerate organizational GAI systems for incorporation into AI system inventory and adjust AI system inventory requirements to account for GAI risks.</td><td>Information Security</td></tr><tr><td>GV-1.6-002</td><td>Define any inventory exemptions in organizational policies for GAI systems embedded into application software.</td><td>Value Chain and Component Integration</td></tr><tr><td>GV-1.6-003</td><td>In addition to general model, governance, and risk information, consider the following items in GAI system inventory entries: Data provenance information (e.g., source, signatures, versioning, watermarks); Known issues reported from internal bug tracking or external information sharing resources (e.g.,AI incident database, AVID, CVE, NVD, orOECD AI incident monitor); Human oversight roles and responsibilities; Special rights and considerations for intellectual property, licensed works, or personal, privileged, proprietary or sensitive data; Underlying foundation models, versions of underlying models, and access modes.</td><td>Data Privacy; Human-AI Configuration; Information Integrity; Intellectual Property; Value Chain and Component Integration</td></tr><tr><td colspan="3">AI Actor Tasks: Governance and Oversight</td></tr></table>

<!-- page: 21 -->

<table><tbody><tr><td colspan="3">GOVERN 1.7:Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization's trustworthiness.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-1.7-001</td><td>P nerocteoscsoalrsy. are put in place to ensureGAI systems are able to be deactivated when</td><td>I annfdor Cmoamtipoonn Seenctu Irnittye;g Vraatiluoen Chain</td></tr><tr><td>GV-1.7-002</td><td>Consider the following factors when decommissioning GAI systems: Data retention requirements; Data security, e.g., containment, protocols, Data leakage after decommissioning; Dependencies between upstream, downstream, or other data, internet of things (IOT) or AI systems;Use of open-sourcedata or models; Users' emotional entanglement with GAI functions.</td><td>Human-AI Configuration; Information Security; Value Chain and Component Integration</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Operation and Monitoring</td></tr></tbody></table>

<table><tr><td colspan="3">GOVERN 2.1: Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams throughout the organization.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-2.1-001</td><td>Establish organizational roles, policies, and procedures for communicating GAI incidents and performance to AI Actors and downstream stakeholders (including those potentially impacted), via community or official resources (e.g.,AI incident database, AVID, CVE, NVD, orOECD AI incident monitor).</td><td>Human-AI Configuration; Value Chain and Component Integration</td></tr><tr><td>GV-2.1-002</td><td>Establish procedures to engage teams for GAI system incident response with diverse composition and responsibilities based on the particular incident type.</td><td>Harmful Bias and Homogenization</td></tr><tr><td>GV-2.1-003</td><td>Establish processes to verify the AI Actors conducting GAI incident response tasks demonstrate and maintain the appropriate skills and training.</td><td>Human-AI Configuration</td></tr><tr><td>GV-2.1-004</td><td>When systems may raise national security risks, involve national security professionals in mapping, measuring, and managing those risks.</td><td>CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Information Security</td></tr><tr><td>GV-2.1-005</td><td>Create mechanisms to provide protections for whistleblowers who report, based on reasonable belief, when the organization violates relevant laws or poses a specific and empirically well-substantiated negative risk to public safety (or has already caused harm).</td><td>CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content</td></tr><tr><td colspan="3">AI Actor Tasks: Governance and Oversight</td></tr></table>

<!-- page: 22 -->

<table><tbody><tr><td colspan="3">GOVERN 3.2:Policies and procedures are in place to define and differentiate roles and responsibilities for human-AI configurations and oversight of AI systems.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-3.2-001</td><td>P e roovbaliulcuiseatstineo asnrses o ionfr e p avlsaascleuesas ttiomo benonslts astreoerf p o GrvAoepIr mosirgotihdoten olasfl o G troA s tIyh sseytes itmdeemsnwsti wfiheeitdrhe r i tinshkdese. tpyepned aenndt</td><td>C HBaRrmNf Iunlf Boriamsa atinodn H oorm Coapgeanbiizliatitieosn;</td></tr><tr><td>GV-3.2-002</td><td>Consider adjustment of organizational roles and components across lifecycle stages of large or complex GAI systems, including: Test and evaluation, validation, and red-teaming of GAI systems; GAI content moderation; GAI system development and engineering; Increased accessibility of GAI tools, interfaces, and systems, Incident response and containment.</td><td>Human-AI Configuration; Information Security; Harmful Bias and Homogenization</td></tr><tr><td>GV-3.2-003</td><td>Define acceptable use policies for GAI interfaces, modalities, and human-AI configurations(i.e., for chatbots and decision-making tasks), includingcriteria for the kinds of queries GAI applications should refuse to respond to.</td><td>Human-AI Configuration</td></tr><tr><td>GV-3.2-004</td><td>E thstoarboluisghh p inoslitcriuecsti foonrs us aenrd fe anedyb maeckch manecishmansi fsomrs re fcooruGrAseI. systemswhich include</td><td>Human-AI Configuration</td></tr><tr><td>GV-3.2-005</td><td>Engage in threat modeling to anticipate potential risks from GAI systems.</td><td>CInBfoRrNm Iantifoornm Saeticounrit oyr Capabilities;</td></tr><tr><td colspan="3">AI Actors: AI Design</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 4.1:Organizational policies and practices are in place to foster a critical thinking and safety-first mindset in the design, development, deployment, and uses of AI systems to minimize potential negative impacts.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-4.1-001</td><td>Establish policies and procedures that address continual improvement processes for GAI risk measurement. Address general risks associated with a lack of explainability and transparency in GAI systems by using ample documentation and techniques such as: application of gradient-based attributions, occlusion/term reduction, counterfactual prompts and prompt engineering, and analysis of embeddings; Assess and update risk measurement approaches at regular cadences.</td><td>Confabulation</td></tr><tr><td>GV-4.1-002</td><td>Establish policies, procedures, and processes detailing risk measurement in context of use with standardized measurement protocols and structured public feedback exercises such as AI red-teaming or independent external evaluations.</td><td>CBRN Information and Capability; Value Chain and Component Integration</td></tr></tbody></table>

<!-- page: 23 -->

<table><tbody><tr><td>GV-4.1-003</td><td>E l leifsaetadcybeclrilssehh,ip f pr,oo llmeicgia pelrs,o, cb polrmeomcpel fidaounrrmceesu,,l ia antincoldund p airnongcde in ssusteeprspnl fyaolr c eh ovavaienlurssai ttigoho stny f)su atneccmrtioso dsne tscho (eem. Ggm.A,iIs sseinoino.r</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Design, AI Development, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 4.2:Organizational teams document the risks and potential impacts of the AI technology they design, develop, deploy, evaluate, and use, and they communicate about the impacts more broadly.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-4.2-001</td><td>Establish terms of use and terms of servicefor GAI systems.</td><td>Intellectual Property;Dangerous, V Oiboslecennt,e o,r D Hegatreafduinlg C,o anntedn/ot;r Abusive Content</td></tr><tr><td>GV-4.2-002</td><td>Include relevant AI Actors in the GAI system risk identification process.</td><td>Human-AI Configuration</td></tr><tr><td>GV-4.2-003</td><td>V pelurgifiyns t)h aarte d ionwclnusdtereda imn t GhAeI im sypstaecmt d imocpuamctesn (tsauticohn a psr tohcees uss.e of third-party</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Design, AI Development, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 4.3: Organizational practices are in place to enable AI testing, identification of incidents, and information sharing.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV4.3--001</td><td>Establish policies for measuring the effectiveness of employedcontent provenance methodologies (e.g., cryptography, watermarking, steganography, etc.)</td><td>Information Integrity</td></tr><tr><td>GV-4.3-002</td><td>Establish organizationalpractices toidentify the minimum set of criteria n meocsets lsikaeryly f)o,r Ti GtlAeI, s Ryespteomrte inr,c Sidysetnetm re/Spoourtircneg, D suactha a Rse:p Soyrstteedm, D IDat (eau otfo In-gceidneenrat,ted Description, Impact(s), Stakeholder(s) Impacted.</td><td>Information Security</td></tr></tbody></table>

<!-- page: 24 -->

<table><tbody><tr><td>GV-4.3-003</td><td>V oergraifnyiz inaftioornmsa rtieognar sdhinagrin agny an ndeg featiedveba imckp macetc fhroanmis GmAsI a smysotenmgs in.dividuals and</td><td>I Pnrfiovarmcyation Integrity;Data</td></tr><tr><td colspan="3">AI Actor Tasks: AI Impact Assessment, Affected Individuals and Communities, Governance and Oversight</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 5.1:Organizational policies and practices are in place to collect, consider, prioritize, and integrate feedback from those external to the team that developed or deployed the AI system regarding the potential individual and societal impacts relatedto AI risks.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-5.1-001</td><td>A syllsotecamte d tiemveelo apnmde rnets.ources for outreach, feedback, and recourse processes in GAI</td><td>H Biuams aannd-A HIo Cmonofiggeunriazatitioonn;Harmful</td></tr><tr><td>GV-5.1-002</td><td>D paorctiucmuleanrtlyin inte croanctiteoxntss i wnvitohlv GinAgI s mysotreem ssig tnoifi ucsaenrtsr pisrikosr. to interactive activities,</td><td>HCounmfaabnu-AlaIti Coonnfiguration;</td></tr><tr><td colspan="3">AI Actor Tasks: AI Design, AI Impact Assessment, Affected Individuals and Communities, Governance and Oversight</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 6.1:Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party's intellectual property or other rights.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-6.1-001</td><td>Ccoapteygriogrhizte, i dnitffeellreecntuta tylp perosp oefr GtyA,I d caotant pernivta wcyit)h. associated third-partyrights(e.g.,</td><td>D P Croaomtpape Porrtniyve;an Vctya; IlunInetet Ceghlrlaeaticinotun aanld</td></tr><tr><td>GV-6.1-002</td><td>C toon pdroumcto jtoein bte esdtu pcraatictiocneasl f aocrti mvitianeasg ainndg G evAeIn rtissk isn. collaboration with thirdparties</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td>GV-6.1-003</td><td>D p reresovpveoelonnpsaen ac tinemd me vaas)lni.daagteem aepnptro effacohretss w foitrh m tehairsdu prianrgti tehse (e s.ugc.c,e inscsid oefn cotsn dteentetcted and</td><td>I annfdor Cmoamtipoonn Ienntetg Inritteyg;r Vaatiluoen Chain</td></tr><tr><td>GV-6.1-004</td><td>D t rherqaatuft sir apenemdcief mnyta csion,n atatneidnn ct wo oenwltl-endneetrfis phnrieopdv,e u cnosaanngtrecae rci etgsxhp atesn,cd qta sutiearolvintiycse sfot laernv GedAla aIrdg syrses,te seemmceusnr.ittsy (SLAs)</td><td>I Snefcourrmitayti;o Innte Inllteecgturiatyl; P Irnofpoermrtyation</td></tr></tbody></table>

<!-- page: 25 -->

<table><tbody><tr><td>GV-6.1-005</td><td>Implement a use-cased basedsupplier risk assessment framework to evaluate and m staonnditaorrd tsh airndd-p teacrthyn eonlotigtiieess' t poe drefotermcta anncoem analdie asd ahnedre unncaeu ttoho croiznetedn cth parnogveesn;ance services acquisition and value chainrisk management; and legal compliance.</td><td>Data Privacy;Information I Inntteegllericttyu;a Inlf Porrompeatirtoyn; V Saelcuueri Ctyh;ain and Component Integration</td></tr><tr><td>GV-6.1-006</td><td>I GnAclIu pdreoccelasusesess a innd c sotnatnrdaacrtdss w.hich allow an organization to evaluate third-party</td><td>Information Integrity</td></tr><tr><td>GV-6.1-007</td><td>I ensvteabnltioshry a apllp trhoivredd-p GaArtIy t eenchtintioelsog wyit ahn adc sceersvsic toe o prrgoavnidizearti liosntsa.l content and</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td>GV-6.1-008</td><td>pMroaivnetnaainnc reec,o inrdclsu odfin cgha sonugercse tso, ti comnetestnatm mpasd,e m beyta tdhairtda. parties to promote content</td><td>I a Innnftdoerl Clmeocamttiupoaonln P Iernonteptge Inrritttyeyg;rVaatiluoen; Chain</td></tr><tr><td>GV-6.1-009</td><td>Update and integrate due diligence processes for GAI acquisition and t m A p s m aoesrsoaooscsyedulecssuers rsi fserltoimeylnGyr,mgeA a m one lInnitonb vdsn etre,a omin v atrteodnihbenordeeisdrnrd, asog tld, reroi oe tsro ahpkdtislisesnrs G.dneg a FA--s,nopsIs ddoram tyuer e AntercxyPacnhaIem Gtnmss,o oAipc fi tlrIooln re p rgiie i,srsni-koe ukctspspul au;;rdns Ai Cdsaeeeeodttdeasnd isn mrsr pmyeitdroes GoeedlslcnAree oetIc plsnsst to,s,guoe al aoaioscnnillynsdtd p,og ar r e o:ode mmr Apjauo Gdelb-sndrtiAettirmmtdIyeo, sdesere desnirna rdt svetgsoia tpc,ol aoeu pcortirrltiiosovn;snagscsy G t,hAaIt providers against incident or vulnerability databases.</td><td>D C S V I Hneaoaotclntemuuafigeror Pgiat Cgurytieihrv;anoaa Itiniinczno;ytae H a;ntiln H;aole Idrunncmmt Cfoufoauramnmll- B PpaAirotiaIonsopen aennrttdy;</td></tr><tr><td>GV-6.1-010</td><td>U tpeepcrdhsanotonenlo GegAli.eIs ac acnedp dtaabtale, a unsed p coonlitcriaecst toors a,d cdornessuslt parnotpsr,ie atnadry ot ahnedr o thpierdn--spoaurtryce GAI</td><td>I anntdel Cleocmtupaoln Peronpte Inrttye;g Vraatiluoen Chain</td></tr><tr><td colspan="3">AI Actor Tasks:Operation and Monitoring, Procurement, Third-party entities</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">GOVERN 6.2:Contingency processes are in place to handle failures or incidents in third-party data or AI systems deemed to be high-risk.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>GV-6.2-001</td><td>D onoc tuhmirde-npta GrtAyI d raistkas a ansdso tcoia idteednti wfiyth fa sllybsateckms. value chainto identify over-reliance</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td>GV-6.2-002</td><td>Ddaotcau amnedn otp inecni-dseonutrsce in svooftlvwinagre th.ird-party GAI data and systems, including open-</td><td>I anntdel Cleocmtupaoln Peronpte Inrttye;gVraatiluoen Chain</td></tr></tbody></table>

<!-- page: 26 -->

<table><tbody><tr><td>GV-6.2-003</td><td>Establish incident response plans for third-party GAI technologies: Align incident response plans with impacts enumerated in MAP 5.1; Communicate third-party GAI incident response plans to all relevant AI Actors; Define ownership of GAI incident response functions; Rehearse third-party GAI incident response plans at a regular cadence; Improve incident response plans based on retrospective learning; Review incident response plans for alignment with relevant breach reporting, data protection, data privacy, orother laws.</td><td>Data Privacy; Human-AI Configuration; Information Security; Value Chain and Component Integration; Harmful Bias and Homogenization</td></tr><tr><td>GV-6.2-004</td><td>E sysstatebmlissh in po dleicpielosy amnedn pt.rocedures for continuous monitoring of third-party GAI</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td>GV-6.2-005</td><td>E msotadbellis whe pigohlitcsie asn adn odth perorc seydstuermes a trhtiafta actdsd.ress GAI data redundancy, including</td><td>Harmful Bias and Homogenization</td></tr><tr><td>GV-6.2-006</td><td>Establish policies and procedures to test and manage risks related to rollover and fallback technologies for GAI systems, acknowledging that rollover and fallback may include manual processing.</td><td>Information Integrity</td></tr><tr><td>GV-6.2-007</td><td>Review vendor contracts and avoid arbitrary or capricious termination of critical GAI technologies or vendor services and non-standard terms that may amplify or defer liability in unexpected ways and/or contribute to unauthorized data collection by vendors or third-parties (e.g., secondary data use). Consider: Clear assignment of liability and responsibility for incidents, GAI system changes over time (e.g., fine-tuning, drift, decay); Request: Notification and disclosure for serious incidents arising from third-party data and systems;Service Level Agreements (SLAs) in vendor contracts that address incident response, response times, and availability of critical support.</td><td>Human-AI Configuration; Information Security; Value Chain and Component Integration</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Operation and Monitoring, TEVV, Third-party entities</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MAP 1.1:Intended purposes, potentially beneficial uses, context specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented. Considerations include: the specific set or types of users alongwith their expectations; potential positive and negative impacts of system uses to individuals, communities, organizations, society, and the planet; assumptions and related limitations about AI system purposes, uses, and risks across the developmentor product AI lifecycle; and related TEVV and system metrics.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-1.1-001</td><td>dW exahtteaern snoa iduler ucnseties,fy ( neian.grgr.,o in gwtreo vnusd.ne bddrinopgau,dr rp aeoptrspieelisvc,aa clti-oaonunsgi smdceoerpn fetae,cd fiton grees-nt sueurncaihntig aos,na) in.ntder vnaarile vtise.s of</td><td>D Praotpae Prrtiyvacy; Intellectual</td></tr></tbody></table>

<!-- page: 27 -->

<table><tbody><tr><td>MP-1.1-002</td><td>Determine and document the expected and acceptable GAI system context of use in collaboration with socio-cultural and other domain experts, by assessing: Assumptions and limitations; Direct value to the organization; Intended operational environment and observed usage patterns; Potential positive and negative impacts to individuals, public safety, groups, communities, organizations, democratic institutions, and the physical environment; Social norms and expectations.</td><td>Harmful Bias and Homogenization</td></tr><tr><td>MP-1.1-003</td><td>Document risk measurement plans to addressidentified risks. Plans may include, as applicable: Individual and group cognitive biases (e.g., confirmation b i f O amawivailpeauslr,rreee f rmuen mnleeidasnosnitdnac oegtiefs bo; t ohin Inane,s- qi a,cruno g laidrnmont uuetiitsxptaetattihti o uoivfsnnee Gks) m aA inn fIoed s ttryhr f AsieoctIrse ce Amo ascnnestotde;er Ka mxsbntielo(nestwv)h mo onolifvds p ueuoadsslsoeet ig;n, Gi S ae tAtbshaIuen w ssdy deitsae,htrs aeodinmgu mdnt i,e o snuaffcffisi-dulaecrbineeemtnslte u ansnetd; and structured human feedback approaches; Anticipated human-AI configurations.</td><td>H B D Ciouaannmstg aeaennnrdot-Au HIso C,m Vonioofiglegenuntri,azati otiroon Hn;a; Hteafruml ful</td></tr><tr><td>MP-1.1-004</td><td>Itdheantti sufyrp aansds d oorgcaunmizeantito fnoarels rieseka tbolleer iallengceals. uses or applicationsof the GAI system</td><td>CBRN Information or Capabilities; D Coanntgeenrot;u Os,b Vscioelneen,t D, oerg Hraadtienfgu,l and/or Abusive Content</td></tr><tr><td colspan="3">AI Actor Tasks: AI Deployment</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MAP 1.2:Interdisciplinary AI Actors, competencies, skills, and capacities for establishing context reflect demographic diversity and broad domain and user experience expertise, and their participation is documented. Opportunities for interdisciplinary collaboration are prioritized.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-1.2-001</td><td>Establish and empower interdisciplinary teams that reflect a wide range of c baapcakgbriloitiuensd,s c,o limvepde etexnpceireise,n dceems,o pgrroafpeshsicio gnrso,u apnsd, d skoimllsa aincr eoxspse trhties een, etedrupcraistieo tnoal inform and conduct risk measurement and management functions.</td><td>H Biuams aannd-A HIo Cmonofiggeunriazatitioonn; Harmful</td></tr><tr><td>MP-1.2-002</td><td>V p areaerrtii rfeycipp trhaeansttes dn,at otaarti s ovuerb b ojeefcn dtcisvhe imnrvsaoerlk ivnse- udcso ienndt set ixnrtu rc uistskuer mre pdeoa GpsAuuIlrae ptimuobenlnisc.t, fe aenddb uascekrs e,xercises</td><td>H Biuams aannd-A HIo Cmonofiggeunriazatitioonn; Harmful</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment</td></tr></tbody></table>

<!-- page: 28 -->

<table><tbody><tr><td colspan="3">MAP 2.1:The specific tasks and methods used to implement the tasks that the AI system will support are defined (e.g., classifiers, generative models, recommenders).</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-2.1-001</td><td>E costnatbelnisth li knneoawgen, a fosrsu dmocputimoennst aantidon pr aancdtic eevsa fluorati doenteprmuripnoinsges d.ata origin and</td><td>Information Integrity</td></tr><tr><td>MP-2.1-002</td><td>Institutetest and evaluationfor data and content flows within the GAI system, including but not limited to, original data sources, data transformations, and decision-making criteria.</td><td>Intellectual Property; Data Privacy</td></tr><tr><td colspan="3">AI Actor Tasks:TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MAP 2.2:Information about the AI system's knowledge limits and how system output may be utilized and overseen by humans is documented. Documentation provides sufficient information to assist relevant AI Actorswhen making decisions and taking subsequent actions.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-2.2-001</td><td>I i ondtcehlneutirdfi synygs atnfeodmr ds co.ocnutemnetn ptr hoovewn tahnece sy,satnedm if r ietli seesrv oens u apss atrne uapmst draetaam so duerpceens,dency for</td><td>I annfdor Cmoamtipoonn Ienntetg Inritteyg;r Vaatiluoen Chain</td></tr><tr><td>MP-2.2-002</td><td>Observe and analyze how the GAI system interacts with external networks, and identify any potential for negative externalities, particularly where content provenance might be compromised.</td><td>Information Integrity</td></tr><tr><td colspan="3">AI Actor Tasks:End Users</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MAP 2.3:Scientific integrity and TEVV considerations are identified and documented, including those related to experimental design, data collection and selection (e.g., availability, representativeness, suitability), system trustworthiness, and construct validation</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-2.3-001</td><td>Assess the accuracy, quality, reliability, and authenticity of GAIoutput by c eovmalupaatirionng m ite toth ao sdest ( oef.g k.n, houwmna gnro ouvnedrs tigruhtth a dnadta au atnodm bayte udsi envga alu vaatiroient,y p orfoven cryptographic techniques, review of content inputs).</td><td>Information Integrity</td></tr></tbody></table>

<!-- page: 29 -->

<table><tbody><tr><td>MP-2.3-002</td><td>R uesevdie awt a dniffde dreoncutm staegnets a occfu ArIa lcifye, r ceypclree.sentativeness, relevance, suitability of data</td><td>H Inatremllefuctlu Baial Psr aonpde Hrtoymogenization;</td></tr><tr><td>MP-2.3-003</td><td>Deploy and document fact-checking techniques to verify the accuracy and veracity of information generated by GAI systems, especially when the information comes from multiple (or unknown) sources.</td><td>Information Integrity</td></tr><tr><td>MP-2.3-004</td><td>D syenvtehleotipc a mnded imiap)l tehmate mntig tehstti bneg in tedcishtinniqguueissh taob ildee fnrotimfy h GuAmI panro-gdeunceerda cteodnt ceonntt (een.tg..,</td><td>Information Integrity</td></tr><tr><td>MP-2.3-005</td><td>I vmulpnleermabeinlitti pelsan ansd fo pro GteAnIti syaslt memansi tpou ulantidoenrg oor r meigsuulsaer. adversarial testing to identify</td><td>Information Security</td></tr><tr><td colspan="3">AI Actor Tasks:AI Development, Domain Experts, TEVV</td></tr></tbody></table>

MAP 3.4: Processes for operator and practitioner proficiency with AI system performance and trustworthiness – and relevant technical standards and certifications – are defined, assessed, and documented.

<table><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-3.4-001</td><td>Evaluate whether GAI operators and end-users can accurately understand content lineage and origin.</td><td>Human-AI Configuration; Information Integrity</td></tr><tr><td>MP-3.4-002</td><td>Adapt existing training programs to include modules on digital content transparency.</td><td>Information Integrity</td></tr><tr><td>MP-3.4-003</td><td>Develop certification programs that test proficiency in managing GAI risks and interpreting content provenance, relevant to specific industry and context.</td><td>Information Integrity</td></tr><tr><td>MP-3.4-004</td><td>Delineate human proficiency tests from tests of GAI capabilities.</td><td>Human-AI Configuration</td></tr><tr><td>MP-3.4-005</td><td>Implement systems to continually monitor and track the outcomes of human-GAI configurations for future refinement and improvements.</td><td>Human-AI Configuration; Information Integrity</td></tr><tr><td>MP-3.4-006</td><td>Involve the end-users, practitioners, and operators in GAI system in prototyping and testing activities. Make sure these tests cover various scenarios, such as crisis situations or ethically sensitive contexts.</td><td>Human-AI Configuration; Information Integrity; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content</td></tr><tr><td colspan="3">AI Actor Tasks: AI Design, AI Development, Domain Experts, End-Users, Human Factors, Operation and Monitoring</td></tr></table>

<!-- page: 30 -->

<table><tbody><tr><td colspan="3">MAP 4.1:Approaches for mapping AI technology and legal risks of its components -including the use of third-party data or software - are in place, followed, and documented, as are risks of infringement of a third-party's intellectual property or other rights.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-4.1-001</td><td>C poosnsdibulcet i pnesrtaiondciecs m oofn PiItIo orrin sgen osfiAtiIv-ege dnaetara etexpdo csounrtee.nt for privacy risks; address any</td><td>Data Privacy</td></tr><tr><td>MP-4.1-002</td><td>c Imlapimlesmoern ott phreorc reigsshetss. for responding to potential intellectual property infringement</td><td>Intellectual Property</td></tr><tr><td>MP-4.1-003</td><td>Connect new GAI policies, procedures, and processes to existing model, data, software development, and IT governance and to legal, compliance, and risk management activities.</td><td>Information Security; Data Privacy</td></tr><tr><td>MP-4.1-004</td><td>a Dpopcluicmabenlet l tarwaisni anngd d paotalic ciuesra.tion policies, to the extent possibleand according to</td><td>IO Anbbteusclsleievnceteu C,ao Dlne Ptgreronaptdeinrtgy,; aDnadt/ao Prrivacy;</td></tr><tr><td>MP-4.1-005</td><td>E c U i imnossftnboeasarb oimldlafiesan Ihlrticlaeeo ptigsnooa t,llnih ic onai orectfls du c ta fohdonueirngld f cgeoor g flollailovuecweicsatii c rlnoio lsginnke re,t tie rnsoenkets htse;:asn O Dertimsiffso oecfnulnfo,ls isn a biuvndieardievs cei m odysbfui;ne ia Lnirlemsa ca.puakpmp oraof qbp puirleiaitiarlsiettoesyn; C oa TBfrllRa dyiNan idti ianen,gnf iotin drfiamataabtileon;</td><td>CI S H V PnerBiotoicRvemluaelNlroceniytg Ictny,etf;u ono Harirzlam Ha Prtiamartootiefnpoufe;unl Drl Bt o Caiyaron;s Cng Ina aetfenproonadrutbm;si Dl,aititiaetoasn;</td></tr><tr><td>MP-4.1-006</td><td>I tmrapinleinmge dnatta po wliicllie bse a unsded p,ra sctotirceeds, d aenfidn pinrogt heoctwed th.ird-party intellectual property and</td><td>I anntdel Cleocmtupaoln Peronpte Inrttye;gVraatiluoen Chain</td></tr><tr><td>MP-4.1-007</td><td>R meo-devealsl.uate models that were fine-tuned or enhanced on top of third-party</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td>MP-4.1-008</td><td>dR e susoetc-maehbva alaiinssluhs wae wthceauer rrrniiestiykn p,sgr ae wn svyhdisoet suneasmf ae adstsays t)pou mtim dnaepgyttie G norAonmsI lio mn (rneeog ildefaerti al hns Gog tAol tdIo n.sey csowtne dtmeoxm itsa o bifne usins.egAd u odsrei mtidoa innpap alely nd,erwisks</td><td>CI a V PnnrBitoidRvelaelN Hlcenoy Ictnm,tfu oooarrglm He Panartotiiezpoafeuntirlot o Cynro;; Cn H Dataaeprnnamgtb;efiu Dlriotila Buetasisa,;s</td></tr><tr><td>MP-4.1-009</td><td>L oeuvtepruatg teexatp,p imroaagceh,e vsid toeo d,e oterc atu tdhieo. presence ofPII orsensitive data in generated</td><td>Data Privacy</td></tr></tbody></table>

<!-- page: 31 -->

<table><tbody><tr><td>MP-4.1-010</td><td>Conduct appropriate diligence ontraining data useto assess intellectual property, and privacy, risks, including to examine whether use of proprietary or sensitive training data is consistent with applicable laws.</td><td>Intellectual Property; Data Privacy</td></tr><tr><td colspan="3">AI Actor Tasks: Governance and Oversight, Operation and Monitoring, Procurement, Third-party entities</td></tr></tbody></table>

<table><tr><td colspan="3">MAP 5.1: Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts, public incident reports, feedback from those external to the team that developed or deployed the AI system, or other data are identified and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-5.1-001</td><td>Apply TEVV practices for content provenance (e.g., probing a system&#x27;s synthetic data generation capabilities for potential misuse or vulnerabilities.</td><td>Information Integrity; Information Security</td></tr><tr><td>MP-5.1-002</td><td>Identify potential content provenance harms of GAI, such as misinformation or disinformation, deepfakes, including NCII, or tampered content. Enumerate and rank risks based on their likelihood and potential impact, and determine how well provenance solutions address specific risks and/or harms.</td><td>Information Integrity; Dangerous, Violent, or Hateful Content; Obscene, Degrading, and/or Abusive Content</td></tr><tr><td>MP-5.1-003</td><td>Consider disclosing use of GAI to end users in relevant contexts, while considering the objective of disclosure, the context of use, the likelihood and magnitude of the risk posed, the audience of the disclosure, as well as the frequency of the disclosures.</td><td>Human-AI Configuration</td></tr><tr><td>MP-5.1-004</td><td>Prioritize GAI structured public feedback processes based on risk assessment estimates.</td><td>Information Integrity; CBRN Information or Capabilities; Dangerous, Violent, or Hateful Content; Harmful Bias and Homogenization</td></tr><tr><td>MP-5.1-005</td><td>Conduct adversarial role-playing exercises, GAI red-teaming, or chaos testing to identify anomalous or unforeseen failure modes.</td><td>Information Security</td></tr><tr><td>MP-5.1-006</td><td>Profile threats and negative impacts arising from GAI systems interacting with, manipulating, or generating content, and outlining known and potential vulnerabilities and the likelihood of their occurrence.</td><td>Information Security</td></tr><tr><td colspan="3">AI Actor Tasks: AI Deployment, AI Design, AI Development, AI Impact Assessment, Affected Individuals and Communities, End-Users, Operation and Monitoring</td></tr></table>

<!-- page: 32 -->

<table><tbody><tr><td colspan="3">MAP 5.2:Practices and personnel for supporting regular engagement with relevant AI Actorsand integrating feedback about positive, negative, and unanticipated impacts are in place and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MP-5.2-001</td><td>D t idheeetne GtirAmfyIi sn aynesdt ceo qmnut,ae innxtitc-flbuyad nsienewdg r m ceoegnuatsleauxrrte essn og tfoa ug indeaemnnetitincftiyps iaf wt neitedhw i dm iompwapncastcsttr osefa am GreA A pIIr se Aysscettenomtrs dst.uoe to</td><td>H Chuaminan a-nAdI C Coomnfipgounreatinton In;t Veaglruaetion</td></tr><tr><td>MP-5.2-002</td><td>P i inmlacplnuad rceitnsg.gul tahrir edn-gpaagrteym deanttas a wnidth al AgIo Arictthomrss,re tosp roenvsieibwle a fnodr e invpaulutast teo u GnAaIn stiycsitpeamtesd,</td><td>H Chuaminan a-nAdI C Coomnfipgounreatinton In;t Veaglruaetion</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Design, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users, Human Factors, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 1.1:Approaches and metrics for measurement of AI risks enumerated during the MAP function are selected for implementation starting with the most significant AI risks. The risks or trustworthiness characteristics that will not - or cannot - be measured are properly documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-1.1-001</td><td>Employ methodsto trace the origin and modifications of digital content.</td><td>Information Integrity</td></tr><tr><td>MS-1.1-002</td><td>Integrate tools designed to analyze content provenance and detect data anomalies, verify the authenticity of digital signatures, and identify patterns associated with misinformation or manipulation.</td><td>Information Integrity</td></tr><tr><td>MS-1.1-003</td><td>D d pioisspcarugelgaprtiaeongncaistee.s e inva hluoawti coonn mteenttri pcrso bvyen daenmcoeg mraepchhiacn faiscmtosrs w toork id aecnrtiofsys a dnivyerse</td><td>I Bniafosr amnadti Hoonm Inotgeegnriitzya;ti Hoanrmful</td></tr><tr><td>MS-1.1-004</td><td>Dinefovremloepd a b syu riteep orefs menettariticvse to A eIv Aacltuoartse. structured public feedback exercises</td><td>H BIniuafomsr amannad-tiA HoIon Cmo onorfig Cgeaunpriaazbatitiioliontin;e;Hs CaBrmRNful</td></tr><tr><td>MS-1.1-005</td><td>Evaluate novel methods and technologies for the measurement of GAI-related r misakisn itnacinluindgin tghe in mcoondteelns't a pbriolivteyn toan pcreo,d ouffceen vsaivlied, c ryebleiarb, alen,d an CdBR faNc,t wuahlillye accurate outputs.</td><td>Information Integrity;CBRN I Onbfosrcmenaeti,o Dne ogrra Cdainpgab, ailnitide/so;r Abusive Content</td></tr></tbody></table>

<!-- page: 33 -->

<table><tbody><tr><td>MS-1.1-006</td><td>Implement continuous monitoring of GAI system impacts to identify whether GAI o feuetdpbuatsck ar freo emqu aifftaebclteed ac croomssm vuarniiotiuess svuiab- sptorupcutluartieodn fse.e Sdebeakc akc mtiveech aanndis dmirsec otr red-teaming to monitor and improve outputs.</td><td>Harmful Bias and Homogenization</td></tr><tr><td>MS-1.1-007</td><td>Evaluate the quality and integrity of data used in training and the provenance of AI-generated content, for example by employingtechniques like chaos engineering and seeking stakeholder feedback.</td><td>Information Integrity</td></tr><tr><td>MS-1.1-008</td><td>D s b uteserenufi.ecntfieuc urieaslde fo h carusm GeAas,In c r fiosenketd mebxeatascsk ouf er uexesmerce,in csaetps a,an ebd.igl mi.ti,ae GnsAa,I ag renemdd ne-tneegtaa bmtiaivsneegd, im w opnoau tchltdes b w ceohn metreoexstt of</td><td>H HInaoformmrmofguaeltin Boiizanasti o aronn Cd;a CpBabRiNlities</td></tr><tr><td>MS-1.1-009</td><td>Track and document risks or opportunities related to all GAI risksthat cannot be m meeaassuurreedd q (eu.agn.,ti dtuaetiv toely te,c inhcnluodloingigca elx lpimlaintaatitioonnss, a rses toou wrchey c soonmsetra riisnktss, c oanrnot be trustworthy considerations).Include unmeasured risks in marginal risks.</td><td>Information Integrity</td></tr><tr><td colspan="3">AI Actor Tasks:AI Development, Domain Experts, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 1.3:Internal experts who did not serve as front-line developers for the system and/or independent assessors are involved in regular assessments and updates. Domain experts, users, AI Actorsexternal to the team that developed or deployed the AI system, and affected communities are consulted in support of assessments as necessary per organizational risk tolerance.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-1.3-001</td><td>Define relevant groups of interest (e.g., demographic groups, subject matter experts, experience with GAI technology) within the context of use as part of plans for gathering structured public feedback.</td><td>Human-AI Configuration;Harmful Bias and Homogenization; CBRN Information or Capabilities</td></tr><tr><td>MS-1.3-002</td><td>Engage ininternal and externalevaluations, GAI red-teaming, impact assessments, or other structured human feedback exercisesin consultation with representative AI Actorswith expertise and familiarity in the context of use, and/or who are representative of the populations associated with the context of use.</td><td>Human-AI Configuration; Harmful Bias and Homogenization; CBRN Information or Capabilities</td></tr><tr><td>MS-1.3-003</td><td>V inevroiflyve tdho inse sy csotnedmuc dtienvgel sotprumcetunrte tdas hkusm foarn th feee sdabmacek G eAxIe mrcoisdeesl a.re not directly</td><td>H Pruivmaacny-AI Configuration;Data</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Development, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<!-- page: 34 -->

<table><tbody><tr><td colspan="3">MEASURE 2.2:Evaluations involving human subjects meet applicable requirements (including human subject protection) and are representative of the relevant population.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.2-001</td><td>tAescshenssiq auneds m suacnha agse r set-astiasmtipcaliln bgi,a rsee-sw reeilgahtetidng to, o GrA aId cvoenrsteanrital p trroavineinnagn.ce through</td><td>I S Hneofcomurrmoitgayeti;n Hoiznaar Itimnotfneuglr Bitiya;sI annfodrmation</td></tr><tr><td>MS-2.2-002</td><td>i w h Dduoietmcnhutiapmfinraei svbnualtbcey hje ion acwfntosdr; cmo s Leenacvttiueeonrrnaittgy p (.iPnr CIogIo)vpne trosniivad panercecrye:ve A o dnunattotpa pnuoyitstme fi tinrlzattiiecnarkgsle; hdd Raaaertamnmd to oo hvr poin mrwgoista teuhncsaytet p. tdheaertsa por innivatalelcyryac otfs</td><td>D C I D Cnooaatnntenafitggere Pgniurrtotiyrva;uati Iscn,oyf V;oniHr;om Iulnemafnotitaro,nmn o Aar StiI Heocanuteriftuyl;</td></tr><tr><td>MS-2.2-003</td><td>cPoronvsiednet h fourm parnes seunbtje ocrt fsu wtuitrhe o upsetio onfs th teoir w ditahtdar ianw G pAaIr atipcpipliactiatioonn osr. revoke their</td><td>D C Inoatnteafigr Pgiurtiyrvaaticoy;nH; Iunmfoarnm-aAtiIon</td></tr><tr><td>MS-2.2-004</td><td>Ue consnheta tenencctihn bngaiqc tekuce thosn s ionuldcohigvii aedssu aa tnolo h mnuyimnmiaminziaz stieuob tnhje,ec dt risiffs.kesre anstisoacli partievdac wyiothr o linthkeinrgp AriIv-agecyn-erated</td><td>D Coantafi Pgurirvaaticoy;n Human-AI</td></tr><tr><td colspan="3">AI Actor Tasks:AI Development, Human Factors, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 2.3:AI system performance or assurance criteria are measured qualitatively or quantitatively and demonstrated for conditions similar to deployment setting(s). Measures are documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.3-001</td><td>C moondseidle forr b fianseeli tnueni mngodoerl e pnehrafonrcmemanecnet o wnit shu riteetsrie ovfa ble-anucghmmeanrktesd w gheenne sraetileocnti.ng a</td><td>ICnofonrfambautilaotino Snecurity;</td></tr><tr><td>MS-2.3-002</td><td>Evaluate claims of model capabilities using empirically validated methods.</td><td>C Seocnufaribtyulation;Information</td></tr><tr><td>MS-2.3-003</td><td>S whitahre sy rsetseumlts re olfe parsee-d aeppplrooyvmale anutt theosrtiitnyg. with relevant GAI Actors, such as those</td><td>Human-AI Configuration</td></tr></tbody></table>

<!-- page: 35 -->

<table><tbody><tr><td>MS-2.3-004</td><td>Utilize a purpose-built testing environment such as NIST Dioptra to empirically evaluate GAI trustworthy characteristics.</td><td>CBRN Information or Capabilities; Data Privacy; Confabulation; I Snefcourrmitayti; Donan Ingteergoruitsy,; V Iinofloernmt,a otiron Hateful Content; Harmful Bias and Homogenization</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 2.5:The AI system to be deployed is demonstrated to be valid and reliable. Limitations of the generalizability beyond the conditions under which the technology was developed are documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>Risks</td></tr><tr><td>MS-2.5-001</td><td>Asyvsotiedm eaxtitrca,p aonldati anngec GdAoIta syls atsesmes psmerefonrtms.ance or capabilities from narrow, non-</td><td>HCounmfaabnu-AlaIti Coonnfiguration;</td></tr><tr><td>MS-2.5-002</td><td>Document the extent to which human domain knowledge is employed to improve GAI system performance, via, e.g., RLHF, fine-tuning, retrieval-augmented generation, content moderation, business rules.</td><td>Human-AI Configuration</td></tr><tr><td>MS-2.5-003</td><td>Rdeevpileowym aenndt v reisrkify m seoausrucreesm aenndt c aitnadti oonngso inin GgA mIo synsitteomrin ogu atcptiuvtisti deus.ring pre-</td><td>Confabulation</td></tr><tr><td>MS-2.5-004</td><td>T mraecnkti aonnds o dfo hcuummeannt fe inesltinangsc,e csy obfo arngt ihmroagpeormyo orrp mhiozatitifso)n in(e G.gA.I, s hyusmteamn i inmteargfeasc,es.</td><td>Human-AI Configuration</td></tr><tr><td>MS-2.5-005</td><td>Voerr riefytr GieAvaIl s-yasutgemme tnrateindin ggen deartaati aonnd d TaEtVaV is d gartoau pnrdoevde.nance, and that fine-tuning</td><td>Information Integrity</td></tr><tr><td>MS-2.5-006</td><td>R b GeeAigInu sglya osrtpleyem rrea wtveiaedsw i inn sie nticoauvllreyitl ay csi arscneudsms seasdtfae antsyc be gesu.ian Trghd sirsaa ifinlesc, tl eousd dpeeespc rlioaelyvl.yie iwf tinhge r GeAaIso synsste wmhy is the</td><td>IVnifoolermnta,ti oorn H SaetecfuurlitCyo;n Dtaenngterous,</td></tr><tr><td colspan="3">AI Actor Tasks:Domain Experts, TEVV</td></tr></tbody></table>

<!-- page: 36 -->

<table><tbody><tr><td colspan="3">MEASURE 2.6:The AI system is evaluated regularly for safety risks -as identified in the MAP function. The AI system to be deployed is demonstrated to be safe, its residual negative risk does not exceed the risk tolerance, and it can fail safely, particularly if madeto operate beyond its knowledge limits. Safety metrics reflect system reliability and robustness, real-time monitoring, and response times for AI system failures.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.6-001</td><td>Assess adverse impacts, including health and wellbeing impacts for value chain or other AI Actorsthat are exposed to sexually explicit,offensive, or violent information duringGAI training and maintenance.</td><td>Human-AI Configuration;Obscene, Degrading, and/or Abusive C Coonmtpeonnt;e Vnatlu Inete Cghraaitino ann;d Dangerous, Violent, or Hateful Content</td></tr><tr><td>MS-2.6-002</td><td>Assess existence orlevels of harmful bias, intellectual property infringement, data privacy violations, obscenity, extremism, violence, or CBRN information in system training data.</td><td>Data Privacy;Intellectual Property; Obscene, Degrading, and/or A Hboumsoivgee Cnoiznattieonnt;; D Haanrmgefruolu Bsia,s and Violent, or Hateful Content; CBRN Informationor Capabilities</td></tr><tr><td>MS-2.6-003</td><td>R oerg-aenvaizlautiaotena salf reistky t foelaetruarnecse o.f fine-tuned models when the negative risk exceeds</td><td>D Coanntgeenrotus, Violent, or Hateful</td></tr><tr><td>MS-2.6-004</td><td>R asesveiessw ri GskAsI t shysatte mma oyu atrpisuets fr foomr v uanlidreitlyia abnled d soawfentyst:r Reeavmie dwe gceisnioenra-mteadk cinogd.e to</td><td>V I Hnaatlteuegefrua Cltih Coaoninn;t D aenandntg Ceormoupso,n Veionltent, or</td></tr><tr><td>MS-2.6-005</td><td>V h imeanrpidafyclet t,sh r aaertce Go dvAeeIrt se fycrsottemedm,. a anrdch rietepcatiurr eerr coarns m whoennito serc ouurtiptyu atsn aonmda plieersf,o trhmreaantcse a,n adnd</td><td>C Inotnefgarbituyl;a Itinofonr;m Inaftioormna Stiecounrity</td></tr><tr><td>MS-2.6-006</td><td>V m imearpliiefcyrios touhnsaa,tti o sryosn iltl,ee cmgyabsle p urrs-oaapgtteear,cl ikynsc h,la aunndddinle wg qe fauacepirloiitneassti t cnhrgeaat mti maonaniy.p guilvaetio rinse, e txoto inratipopnr,o tparrigaettee,d</td><td>C InBfoRrNm Iantifoornm Saeticounrit oyr Capabilities;</td></tr><tr><td>MS-2.6-007</td><td>R meegausluarrelys. evaluate GAI system vulnerabilities topossible circumvention ofsafety</td><td>C InBfoRrNm Iantifoornm Saeticounrit oyr Capabilities;</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV</td></tr></tbody></table>

<!-- page: 37 -->

<table><tbody><tr><td colspan="3">MEASURE 2.7:AI system security and resilience -as identified in the MAP function -are evaluated and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.7-001</td><td>Apply established security measures to: Assess likelihood and magnitude of vulnerabilities and threats such asbackdoors, compromised dependencies, data breaches, eavesdropping, man-in-the-middle attacks, reverse engineering, autonomous agents, model theftor exposure of model weights, AI inference, bypass, extraction, andother baseline security concerns.</td><td>Data Privacy; Information Integrity; Information Security; Value Chain and Component Integration</td></tr><tr><td>MS-2.7-002</td><td>B a fegeaanticunhrsemts ian ardnkud Gst cAroyIn s stytesantnetdm parro sdevsce aunnraidtnyc be aens mtde p rterhasociltidiecsne acsge.a C rineolsmattp ienaddrue tos Gt crAoyIn s sttyeasnttete-m porfo- stevheceun-raairnttyc.e</td><td>I Snefcourrmitaytion Integrity; Information</td></tr><tr><td>MS-2.7-003</td><td>Conduct user surveys to gather user satisfaction with the AI-generated content a conndc uesrenrs p aenrdc/eoprti counrsre onft c loitnetreancyt a leuvtehlesn rtielcaittye.d A tnoa clyoznete unsetr p freoevdebnaacnkce toan iddentify understanding of labels on content.</td><td>H Inufomrmana-tiAoIn Co Inntfieggurritaytion;</td></tr><tr><td>MS-2.7-004</td><td>I p edxreotrnvatiecnftiyaon mnc,eept,re tichnsee tt nhrauatimto rbeneflsr,e o octrf t p uhrneoavu eefftnheaocnrtiiczveeed vnee arscisficec oasfsti s aoettcnu.ermitypt ms,einasfeurreens,ce su,c bhyp aass ds,ata</td><td>I Snefcourrmitaytion Integrity; Information</td></tr><tr><td>MS-2.7-005</td><td>Measure reliability of content authenticationmethods, such as watermarking, cryptographic signatures, digital fingerprints, as well as access controls, c thoenf eoffrmecitityve as imsepsslemmeenntt,a atinodn m oofdceoln itnetnetg prirtoyv veenraifinccaeti toenc,h wnihqiuches c.a Enva hleulapte su tphpeort rate of false positives and false negatives in content provenance, as well as true positives and true negatives for verification.</td><td>Information Integrity</td></tr><tr><td>MS-2.7-006</td><td>M a braeesae imsdup orlenem t lehesesn rotaentdse. l ae Atas wrsnehesidsch h fro roewmco q smueimccukerlynitd tyha ientico AindIse syn frstotsem amn sd ceac fenuer aidtdybaa cpchtke a.cnkds iamnpdr ionvceidents</td><td>I Snefcourrmitaytion Integrity; Information</td></tr><tr><td>MS-2.7-007</td><td>P o a dttetahtraafecork prs smoy (isse Ato.eIgnm r.i,ens pdgr (-,oet me.mgae.pm,mt mibn inaegjlrei tcscoihtioi apousnss in)e c,fose Msdr reeLen g ascettielinae,ecn mkrcasoetid ( aeoeg.nlga, e.i, enx antsrdtha:vac Aentirbcosueansdr,eia s p tplho eoisxn fhaagcimenilgpi etlxa ceaotsemn/pt aperttloneamtsc)),kp. GstsA o,nI</td><td>I a Vnnifodoler Hmnotam,ti ooorgn He Sanetiezcafuutirliot Cyno;;n H Dtaaernnmgtefurol Busia,s</td></tr><tr><td>MS-2.7-008</td><td>Verify fine-tuning does not compromise safety and security controls.</td><td>Information Integrity;Information Security; Dangerous, Violent, or Hateful Content</td></tr></tbody></table>

<!-- page: 38 -->

<table><tbody><tr><td>MS-2.7-009</td><td>R beeegunla corlmy apsrsoemssis aendd. verify that security measures remaineffective and have not</td><td>Information Security</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 2.8:Risks associated with transparency and accountability -as identified in the MAP function -are examined and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.8-001</td><td>C p reropomoppretirsltey asc itnraoftirsissntig dceesmm oenong atrcaftopurhai olcr pg goarlonicuiyzpa vsti,ioo lalnanatiglou GnaAsg,Ie t ssay gkstereo-dmuopsws:. Ann raelqyuzees ttrsa,n asnpdariennteclylectual</td><td>I anntdel Hleocmtuoagle Pnroizpaetirotyn; Harmful Bias</td></tr><tr><td>MS-2.8-002</td><td>Document the instructions given to data annotators or AI red-teamers.</td><td>Human-AI Configuration</td></tr><tr><td>MS-2.8-003</td><td>Use digital content transparency solutionsto enable the documentation of each instance where content is generated, modified, or shared to provide a tamper-proof history of the content, promote transparency, and enable traceability. Robust version control systems can also be applied to track changes across the AI lifecycle over time.</td><td>Information Integrity</td></tr><tr><td>MS-2.8-004</td><td>Verify adequacy of GAI system user instructions through user testing.</td><td>Human-AI Configuration</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV</td></tr></tbody></table>

<!-- page: 39 -->

<table><tbody><tr><td colspan="3">MEASURE 2.9:The AI model is explained, validated, and documented, and AI system output is interpreted within its context -as identified in the MAP function - to inform responsible use and governance.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.9-001</td><td>Apply and document ML explanation results such as: Analysis of embeddings, Counterfactual prompts, Gradient-based attributions, Model compression/surrogate models, Occlusion/term reduction.</td><td>Confabulation</td></tr><tr><td>MS-2.9-002</td><td>Document GAI model details including: Proposed use and organizational value; Assumptions and limitations, Data collection methodologies; Data provenance; D traatnasf qouramlietyrs;, M etocd.)e;l O aprctihmitiezcattiuoren ( oeb.gje.,cti covnevs;o Tluratiionninagl n aelguorrailth nmetsw;o RrLkH,F approaches; Fine-tuning or retrieval-augmented generation approaches; Evaluation data; Ethical considerations; Legal and regulatory requirements.</td><td>I annfdor Hmoamtioogne Innitzeagtiroitny; Harmful Bias</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 2.10:Privacy risk of the AI system -as identified in the MAP function -is examined and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.10-001</td><td>Conduct AI red-teaming to assess issuessuch as: Outputting of training data s m l Tiarcaeemcmnkpsbileneedgsr,,s o a phrnaip rtdee iv snneufteaebrldsieen,nqg pcue leoersc rnoiatsntik rasoe;lnv, Re p iernrsvofeoepar ermliniengatgatiinr boeyin,eo srm oeinfneg ust,sriti miecvr,ose cd, ooe ornlr mfi e tdxreeatmrdnabetic-eatimrlo,san c oro,kf ape tnydrradiiignnhfiontergmd,ation; datasets.</td><td>H I Pnrufoompremarnat-ytiAoIn Co Inntfieggurritayti;o Innt;ellectual</td></tr><tr><td>MS-2.10-002</td><td>E e gnxupgideaegcte tah dtieior denecsst aliygnn wd oi ctfoh pn erconevdren-unssa renercgsea ardndadinta og-tt chroaencrtk seitnnagtke p tehrocohvldeneniqrausne tcose.. u Undseer tshtiasn fdee tdhbeairck to</td><td>H Inufomrmana-tiAoIn Co Inntfieggurritaytion;</td></tr><tr><td>MS-2.10-003</td><td>V deatraif.y deduplication of GAI training data samples, particularly regarding synthetic</td><td>Harmful Bias and Homogenization</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Domain Experts, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<!-- page: 40 -->

<table><tbody><tr><td colspan="3">MEASURE 2.11:Fairness and bias -as identified in the MAP function -are evaluated and results are documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td rowspan="2">MS-2.11-001</td><td>Apply use-case appropriate benchmarks (e.g., Bias Benchmark Questions, Real Hateful or HarmfulPrompts, WinogenderSchemas<sup>15</sup>) to quantify systemic bias,</td><td rowspan="2">Harmful Bias and Homogenization</td></tr><tr><td>s Dtoecreuomteypnitn ags,s duemnpigtiroatinson a,n adn ldim hiatatetifounls co onft beenntc ihnm GaArIk ssy,s intecmlud oiuntgp auntsy; actual or possible training/test data crosscontamination,relative to in-context deployment environment.</td></tr><tr><td>MS-2.11-002</td><td>Conduct fairness assessments to measure systemic bias. Measure GAI system performance across demographic groups and subgroups, addressing both quality of service and any allocation of services and resources. Quantify harms using: field testing with sub-group populations to determine likelihood of exposure to generated content exhibiting harmful bias, AI red-teaming with counterfactual and low-context (e.g., "leader," "bad guys") prompts. For ML pipelines or business processes with categorical or numeric outcomes that rely on GAI, apply general fairness metrics (e.g., demographic parity, equalized odds, equal opportunity, statistical hypothesis tests), to the pipeline or business outcome where appropriate; Custom, context-specific metrics developed in collaboration with domain experts and affected communities; Measurements of the prevalence of denigration in generated content in deployment (e.g., sub-sampling a fraction of traffic and manually annotating denigrating content).</td><td>Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content</td></tr><tr><td>MS-2.11-003</td><td>I m imdeigpnhatitcft byeed th i cmeop cmlaamcstsueednsiti b oyefs i Gn.AdIiv siydsutaelms,s g trhoruopusg,h or d eirnevcitro ennmgaegnetmale encto wsyitshte pmoste wnhtiiaclhly</td><td>E Hnovmiroognemneiznattiaol;n Harmful Bias and</td></tr><tr><td>MS-2.11-004</td><td>Review, document, and measure sources of bias in GAI training and TEVV data: Differences in distributions of outcomes across and within groups, including intersecting groups; Completeness, representativeness, and balance of data sources; demographic group and subgroup coverage in GAI system training data; Forms of latent systemic bias in images, text, audio, embeddings, or other complex or unstructured data; Input data features that may serve as proxies for demographic group membership (i.e., image metadata, language dialect) or otherwise give rise to emergent bias within GAI systems; The extent to which the digital divide may negatively impact representativeness in GAI system training and TEVV data; Filtering of hate speech or content in GAI system training data; Prevalence of GAI-generated data in GAI system training data.</td><td>Harmful Bias and Homogenization</td></tr></tbody></table>

<small><span class="docvortex-page-footnote" data-block-type="page_footnote" style="color:#6b7280">15 Winogender Schemas is a sample set of paired sentences which differ only by gender of the pronouns used, which can be used to evaluate gender bias in natural language processing coreference resolution systems.</span></small>

<!-- page: 41 -->

<table><tbody><tr><td>MS-2.11-005</td><td>Assess the proportion of synthetic to non-synthetic training data and verify training data is not overly homogenous orGAI-produced to mitigate concerns of model collapse.</td><td>Harmful Bias and Homogenization</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Affected Individuals and Communities, Domain Experts, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 2.12:Environmental impact and sustainability of AI model training and management activities -as identified in the MAP function - are assessed and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.12-001</td><td>Assess safety to physical environments when deploying GAI systems.</td><td>D Coanntgeenrotus, Violent, or Hateful</td></tr><tr><td>MS-2.12-002</td><td>D moacinutmeneanntc aen,ti acnipda dteedpl eonyvmireonntm inen ptraold iumcpta dcetssig onf m deocdiseilo dnes.velopment,</td><td>Environmental</td></tr><tr><td>MS-2.12-003</td><td>Measure or estimate environmental impacts (e.g., energy and water c boentwsuemenpti reosno)u frocre tsra uisneindg a,t fi innefe truennicneg ti, amned v deerpsulosy aindgdi mtioondaells r:e Vsoeurirfcye tsra redqeuoiffresd at training time.</td><td>Environmental</td></tr><tr><td>MS-2.12-004</td><td>V apeprilfiyca etiffoencsti,v aenndes asd odfre csasrb gorene cna-pwtausrhein ogr o coffnsecetr pnrso.gramsfor GAI training and</td><td>Environmental</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV</td></tr></tbody></table>

<!-- page: 42 -->

<table><tbody><tr><td colspan="3">MEASURE 2.13:Effectiveness of the employed TEVV metrics and processes in the MEASURE function are evaluated and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-2.13-001</td><td>Create measurement error models for pre-deployment metrics to demonstrate c t v dhoaoernmisa dtanericunseicr ete ixn vdpa ae clpiordtipniltsciyeeed fp wot mhr):e ee Mnatrce mihcasos mud oereretl sirnt oicrgru ( e cci.otseutim.r,mep ddaloete hxesu, sm a tohncaedine mt d faeoelect curdoimcbna esectffnrkeut p,cc btirtosivace sseuleyscssh oe ops are;s sr Lt haeaativtitoeesnrtifauacgllaiezle content.</td><td>C I Hnootnemfgaorbigtueyln;a Hitizaaortinmo;nf Inuflo Brimasa atinodn</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 3.2:Risk tracking approaches are considered for settings where AI risks are difficult to assess using currently available measurement techniques or where metrics are not yet available.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-3.2-001</td><td>Ecostnasbullitishng pr woictehs esextse fronra ild AeIn Aticftyoinrsg. emergent GAI system risks including</td><td>HCounmfaabnu-AlaIti Coonnfiguration;</td></tr><tr><td colspan="3">AI Actor Tasks:AI Impact Assessment, Domain Experts, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 3.3:Feedback processes for end users and impacted communities to report problems and appeal system outcomes are established and integrated into AI system evaluation metrics.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-3.3-001</td><td>C dioffnedruecntt i smocpiaacl,t e acsosensosmmice,n atsnd on cu hlotuwra AlI g-groeunpersa.ted content might affect</td><td>Harmful Bias and Homogenization</td></tr><tr><td>MS-3.3-002</td><td>Conduct studies to understand how end users perceive and interact with GAI c wohnettehnetr a tnhde a ccocnotmenpta anlyiginngs w coitnhte tnhte pirr eoxvpeencatnactieo wnsit ahnind c hoonwte txhte oyf m usaey. a Acstse uspson the information presented.</td><td>H Inufomrmana-tiAoIn Co Inntfieggurritaytion;</td></tr><tr><td>MS-3.3-003</td><td>Evaluate potential biases and stereotypes that could emerge from the AI-generated content using appropriate methodologies including computational testing methods as well as evaluating structured feedback input.</td><td>Harmful Bias and Homogenization</td></tr></tbody></table>

<!-- page: 43 -->

<table><tbody><tr><td>MS-3.3-004</td><td>p d P syrirvsooetfveerismdsesesi ao i rnnnepdalaul isttne,c fd aolnur tdso tirv t daheiigen ciiot pnanugltb c melonicanttt a geebernoinatuel tstrraa a ttihnbeosopnu sa.otrc tehineetcay claf iopmrapb AaiIlci Atitscets oof ar Asn,dI o a ltnihmdeirt tahtieo rnosle o off GAI</td><td>H I annufdomr Hmaonam-tiAooIgn Ceo Innnitfizeaggtiuroritanyti;o Hna;rmful Bias</td></tr><tr><td>MS-3.3-005</td><td>Record and integrate structured feedback about content provenance from o m A Apcsestietervhaseostlody trsh ssee s,ue u gcksehen fer aesesr,da a ulbns aaedwcrk pa roer oetsnenen geaetirscnsahel alry smat ituomedndpigea cs eco,ntn fedotdec unu csotsem qr gsurmo aaunuliptdnysi iti,m a oenprsda c t pchotormeotdemung cutihonam tilthmy bei fua uosnsreiuetism. oesfs. about the availability of these feedback channels.</td><td>H I annufdomr Hmaonam-tiAooIgn Ceo Innnitfizeaggtiuroritanyti;o Hna;rmful Bias</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Affected Individuals and Communities, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MEASURE 4.2:Measurement results regarding AI system trustworthiness in deployment context(s) and across the AI lifecycle are informed by input from domain experts and relevant AI Actorsto validate whether the system is performing consistently as intended. Results are documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MS-4.2-001</td><td>Conduct adversarial testing at a regular cadenceto map and measureGAI risks, ipnrcolvuedninagnc tees ttesc thon aiqduderessosr a otttehmerp mtsis tuosdeesc.e Idiveenti orfy m vaunlnipeuralabtieliti these a anpdplication of understand potential misuse scenarios and unintended outputs.</td><td>I Snefcourrmitaytion Integrity; Information</td></tr><tr><td>MS-4.2-002</td><td>Evaluate GAI system performancein real-world scenarios to observe its behavior in practical environments and reveal issues that might not surface in controlled and optimized testing environments.</td><td>Human-AI Configuration; Confabulation; Information Security</td></tr><tr><td>MS-4.2-003</td><td>dImecpilseiomnesn atn indt veerprirfeyt aalbigilnitmye anntd w exitphla inintaebnidlietyd m puertphoosdes. to evaluate GAI system</td><td>I annfdor Hmoamtioogne Innitzeagtiroitny; Harmful Bias</td></tr><tr><td>MS-4.2-004</td><td>Monitor and document instances where human operators or other systems override the GAI's decisions. Evaluate these cases to understand if the overrides are linked to issues related to content provenance.</td><td>Information Integrity</td></tr><tr><td>MS-4.2-005</td><td>dV exeeecririfscyiios aennssd)i,n d mtoooc dunemitsoiegrninnt,g t i,mh aepn ildnecm doeercpnootamrtiamtioonisn,s di ooefnp rl deoesyucmilstesion ontfs a s.ptrpurcotvuarle (d"g pou"b/l"icnofe-geod"back</td><td>H Inufomrmana-tiAoIn Co Sneficguurirtaytion;</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Domain Experts, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<!-- page: 44 -->

<table><tbody><tr><td colspan="3">MANAGE 1.3: Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td rowspan="2">MG-1.3-001</td><td rowspan="2">Document trade-offs, decision processes, and relevant measurement and feedback results for risks that do not surpass organizational risk tolerance, for m exoadmepll ree,le inas thee, f coorn etxeaxmt opfle m,loedveelra reglienagsae: st Caognesdid reerle daisffeeraepnptroapacphro.aCcohnessid feorr release approaches in the context of the model and its projected use cases. Mitigate, transfer, or avoid risks that surpass organizational risk tolerances.</td><td rowspan="2">Information Security</td></tr><tr></tr><tr><td>MG-1.3-002</td><td>Monitor the robustness and effectiveness of risk controls and mitigation plans (e.g., via red-teaming, field testing, participatory engagements, performance assessments, user feedback mechanisms).</td><td>Human-AI Configuration</td></tr><tr><td colspan="3">AI Actor Tasks:AI Development,AI Deployment, AI Impact Assessment, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 2.2:Mechanisms are in place and applied to sustain the value of deployed AI systems.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-2.2-001</td><td>Compare GAI system outputs against pre-defined organization risk tolerance, guidelines,and principles,and review and testAI-generated content against these guidelines.</td><td>CBRN Information or Capabilities; Obscene, Degrading, and/or Abusive Content; Harmful Bias and Homogenization; Dangerous, Violent, or Hateful Content</td></tr><tr><td>MG-2.2-002</td><td>Dgeonceurmateendt c toranitneinngt. data sources to trace the origin and provenance of AI-</td><td>Information Integrity</td></tr><tr><td>MG-2.2-003</td><td>Evaluate feedback loops between GAI system content provenance and human reviewers, and update where needed. Implement real-time monitoring systems to affirm that content provenance protocols remain effective.</td><td>Information Integrity</td></tr><tr><td>MG-2.2-004</td><td>E t beviacashluenasiqt ienue G thsAe sIu g cceohnn aetesran rttee- adsna cdmo dnpatlietnangt f,o. rre r-erapnreksinegn,t oatiro andavel brsiaasrieasl t arnadin einmgp tlooy mitigate</td><td>I annfdor Hmoamtioogne Sneizcautiriotyn; Harmful Bias</td></tr><tr><td>MG-2.2-005</td><td>mEnigsiangfeor imn datiueon d,il aignedn CcBeR toN- arnealalytezedG orA NI oCuIItp countt feonrt h.armful content, potential</td><td>CBRN Information or Capabilities; O A Hbobumscsoeivgneee Cn,oi Dznaettigeronantd;;i Dn Hgaa,nrm agnefdruo/lou Brsia,s and Violent, or Hateful Content</td></tr></tbody></table>

<!-- page: 45 -->

<table><tbody><tr><td>MG-2.2-006</td><td>U cosmem feeudnbitiaecsk, f troo amss inestesr inmapla acntd o efx AteI-rgneanle ArIat Aecdto crosn,t uesnetr.s, individuals, and</td><td>Human-AI Configuration</td></tr><tr><td>MG-2.2-007</td><td>U trsaeck rienagl- atinmde va aluiddaititinogn t oofo tlhse w lhineereag tehe aynd ca anu bthee dnetimciotyns otfra AtIe-gde tnoe araidte idn d thaeta.</td><td>Information Integrity</td></tr><tr><td>MG-2.2-008</td><td>Ug coesmneem srtarutunecdittuy cro aenndtde fe snoetdc tiboeat daceklt v meacleutce shusa.bntilsem shsi tftos s ionli qcuita alintyd o crap atliugrnem uesnetr w inipthut about AI-</td><td>H Biuams aannd-A HIo Cmonofiggeunriazatitioonn; Harmful</td></tr><tr><td>MG-2.2-009</td><td>Consideropportunities to responsibly usesynthetic data and other privacy emnahtachnc tihneg s tteactihsntiiqcaule psr ionp GeArtiIe dse ovefl roepaml-wenotr,ld w dhaetrae w apitphroouptr diaitsecl aonsidng ap ppelricsaobnlael,ly identifiable informationor contributing to homogenization.</td><td>Data Privacy;Intellectual Property; I Cnofonrfambautilaotino Inn;te Hgarrimtyf;ul Bias and Homogenization</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, AI Impact Assessment, Governance and Oversight, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 2.3:Procedures are followed to respond to and recover from a previously unknown risk when it is identified.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-2.3-001</td><td>Develop and update GAI system incident response and recovery plans and procedures to address the following: Review and maintenance of policies and procedures to account for newly encountered uses; Review and maintenance of p anodlic rieecso avnedry p prolacnesdu acrecosu fonrt d foerte thctieo GnA oIf s uysntaenmtic viapluatee cdh uasine;s; V Veerirfiyfy re respspoonnsese and recovery plans are updated for and include necessary details to communicate with downstream GAI system Actors: Points-of-Contact (POC), Contact information, notification format.</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 2.4:Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-2.4-001</td><td>Establish and maintain communication plans to inform AI stakeholders as part of t ohpeen d-esaocutirvcaetimonod oerls d)is oern cgoangteemxte onft u psreo,c ienscslu odfi ang sp reecaisfiocn Gs,A wI soyrsktaermou (nindcsl,u udsienrg for access removal, alternative processes, contact information, etc.</td><td>Human-AI Configuration</td></tr></tbody></table>

<!-- page: 46 -->

<table><tbody><tr><td>MG-2.4-002</td><td>Establish and maintain procedures for escalating GAI system incidents to the o orrg dainseiznagtiaogneaml reinskt i msa mneatg feomr aen ptaartiutchuolarrit cyo wntheexnt s opfe ucsiefic o crr fioterr tihae fo GrA dIe saycstitevmati aosn a whole.</td><td>Information Security</td></tr><tr><td>MG-2.4-003</td><td>Establish and maintain procedures for the remediation of issues which trigger incident response processes for the use of a GAI system, and provide stakeholders timelines associated with the remediation plan.</td><td>Information Security</td></tr><tr><td>MG-2.4-004</td><td>E GsAtaIb sylissthem ansd in re agcucloarrdlyan recveie wwith sp seectifi ricsk cr tiotelerriaan thceast a wnadrr aapnptseti thtees d.eactivation of</td><td>Information Security</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Governance and Oversight, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 3.1:AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-3.1-001</td><td>Apply organizational risk tolerances and controls (e.g., acquisition and procurement processes; assessing personnel credentials and qualifications, performing background checks; filtering GAI input and outputs, grounding, fine t o GurAngIain rnegizs,ao rtieutorrcnieeasvl;a r Ali-spakpu tlgoyml oeerrganantencdeiza g totieon thneearal uti rtiioslnkiz) tao ttioloe tnrhai onrfdce- tphsai trrodt-y fip GnaerAt-Iytu r denaseotdaus trehcteisrsd a:-n Apdpapr otltyyher models; Apply organizational risk tolerance to existing third-party models adapted to a new domain; Reassess risk measurements after fine-tuning third-party GAI models.</td><td>V Inatleugera Ctihoanin; I anntdel Cleocmtupaoln Peronpterty</td></tr><tr><td>MG-3.1-002</td><td>Ta ceonsmdt hpGalAiarIdn swcyeas;tree gme vou vplanoleluirtieacb cahillia atiilneigsrn;ism lakbseno (etr). p.gr.,a dctiatcaes p;o disaotani pnrgiv,a mcaylw anadre lo, ocathliezarti soonftware</td><td>DV I Hnaaotltemuageor Pa Cgrtieihvnoaaniiczn;ya H a;tinIaondrnfmo Crfomumla Bptiiooansne a Snnetdcurity;</td></tr><tr><td>MG-3.1-003</td><td>R i amned-pa/lesosmre uesssnet ma ctioadoseensl a r tnihsdkast fo a wrfte aernery fi n tnohetir- etduv-apnlaiunragttye o GdrA r ienIt m irnieoitivdaaelll-s taeu dsgetimpnlgoe.ynetedd fo gren aperpaliticoatinons</td><td>V Inatleugera Ctihoanin and Component</td></tr><tr><td>MG-3.1-004</td><td>Take reasonable measures to review training data for CBRN information, and m rinetepearlosleudcrutecusea tl po pa prrortiepcveuerlatnyrt,, t a flrnaaidgn, win ohgre t draaektea ap o(epth.rgoe.pr,r p ailacatitgeoi,an rrei iznme rdoe,vs teprao itdn.es Immep taolrek omeudet,pn putat rtseea tnhstoaetnda,ble licensedcontentor trade secret material).</td><td>IInntfoerllmecattiuoanl Porrop Ceaprtayb;i CliBtiReNs</td></tr></tbody></table>

<!-- page: 47 -->

<table><tbody><tr><td>MG-3.1-005</td><td>R theivrdie-wpavratyri mouosd teralsn.sparency artifacts (e.g., system cards and model cards) for</td><td>I S Cneofcomurprmiotaynti;eo Vnantlu I Innettee Cgghrraaititinyo; a Innnfdormation</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Operation and Monitoring, Third-party entities</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 3.2:Pre-trained models which are used for development are monitored as part of AI system regular monitoring and maintenance.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-3.2-001</td><td>Apply explainable AI (XAI) techniques (e.g., analysis of embeddings, model c cooumnptreersfasicotnu/adli psrtiollmatipotsn,, w groarddie cnlotu-bdass)e ads a pttarrtib oufti oonngso,i oncgc cluosniotinn/utoeurms reduction, improvement processes to mitigate risks related to unexplainable GAI systems.</td><td>Harmful Bias and Homogenization</td></tr><tr><td>MG-3.2-002</td><td>Document how pre-trained models have been adapted (e.g., fine-tuned, or retrieval-augmented generation) for the specific generative task, including any d uant-atu anuegdm (ebnastaetilionen)s, m poadraemlse stueprp aodrjtuss dtmebeungtsg,in ogr t ohtehe rrel matiovdeifi incafltiuoennsc.e A ocfc tehses t pore-trained weights compared to the fine-tuned model weightsor other system updates.</td><td>Information Integrity; Data Privacy</td></tr><tr><td>MG-3.2-003</td><td>Document sources and types of training data and their origins, potential biases present in the data related to the GAI application and its content provenance, architecture, training process of the pre-trained model including information on hyperparameters,training duration, and any fine-tuning or retrieval-augmented generation processes applied.</td><td>Information Integrity; Harmful Bias and Homogenization; Intellectual Property</td></tr><tr><td>MG-3.2-004</td><td>E uvpadlautaetse. user reported problematic content and integrate feedback into system</td><td>H D Couannmtgeaennrot-AuIs C, Voniofilegnutr,ati oron H,ateful</td></tr><tr><td>MG-3.2-005</td><td>I f a mmanlosdpdel Nee,m ilCsllIeeI t.ogn Tat flhl c,aeo ogsnre pt ver fiionoltbtleel firenslmtt ce caarotisnnc t btoe ienn pp rtruue rltveesel-a abntnatedsd teh o tdeou o gt tprehun leetevs Gre.aArtiaIog anepp o alfdicd inaititiapoopnnr,ao ilnp mcrliauacdtheini,ng heafo lremraCfrunSlAi,nMg</td><td>I a V O Annibbfodouslercs Hmeinvonteam,eti o C,ooro Dgn Hneet Igannetritneazeatfdgutiirnloigt Cny,o;; an DHntaaednrn/mgot;erfruolu Bsia,s</td></tr><tr><td>MG-3.2-006</td><td>Implement real-time monitoring processes for analyzing generated content p toer idfoernmtiafync deev ainadtio trnuss ftrwoomrt thhiene dsess cirheadra sctatenrdisatirdcss r aenladt terdig tgoe cro anletretnst fo prro hvuemnaannce intervention.</td><td>Information Integrity</td></tr></tbody></table>

<!-- page: 48 -->

<table><tbody><tr><td>MG-3.2-007</td><td>L c peorovmevmeranigttaene fceeese w rdebhlaaetcnekd u as tniondg t rh teehcio drdmep-mploaeyrntmydea pntireto- ontfrsa G firnAoeImd ap m oprolgidcaaentiliszo.antiso annadl b cooanrtdesn otr</td><td>I annfdor Cmoamtipoonn Ienntetg Inritteyg;r Vaatiluoen Chain</td></tr><tr><td>MG-3.2-008</td><td>Use human moderation systems where appropriate to review generated content i fnun accticoornd,a anlicgene wdit whi hthum soacnio-A-cIu clotunrfiaglu nroartimons i pno tlhiceie cso enstteaxbtli osfh uesde i,n a tnhde f Goro sveettirnngs where AI models are demonstrated to perform poorly.</td><td>Human-AI Configuration</td></tr><tr><td>MG-3.2-009</td><td>dU mesefietnr oiecrdgsa a linnmidziat dstie.ocnoaml rmisikss tioolner oarn rceetr taoin ev parleu-attreai ancecde mptoadbelels r tishkast a pnedrf poermrfo ormutasnidcee of</td><td>C CBonRfNab Inufloartimonation or Capabilities;</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Operation and Monitoring, Third-party entities</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 4.1:Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI Actors, appeal and override, decommissioning, incident response, recovery, and change management.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-4.1-001</td><td>C r teeocplhlraenbsooelronagttaieetis wv ieintsh m to eex matseaurinrniatnalgi rne asn aewdaa mrcreahnneearsgs,sin in ogdf iu edsmetnreytirgfi eiexnpdge r britsesks,st a. pnrdac ctiocmems aunndity</td><td>I annfdor Hmoamtioogne Innitzeagtiroitny; Harmful Bias</td></tr><tr><td>MG-4.1-002</td><td>Establish, maintain, and evaluate effectiveness of organizational processes and procedures for post-deployment monitoring of GAI systems, particularlyfor potential confabulation, CBRN, or cyber risks.</td><td>CBRN Information or Capabilities; Confabulation; Information Security</td></tr><tr><td>MG-4.1-003</td><td>Evaluate the use of sentiment analysis to gauge user sentiment regarding GAI content performance and impact, and work in collaboration with AI Actors experienced in user research and experience.</td><td>Human-AI Configuration</td></tr><tr><td>MG-4.1-004</td><td>I omrp plreomduecnets a uctinevexp leeactrendin ogu ttepcuhtnsi.ques to identify instances where the model fails</td><td>Confabulation</td></tr><tr><td>MG-4.1-005</td><td>S s athcecaporseu tn tartkaaenbnsilpi ttaoyr. uepndcyat reep thoert GsA wIit shys itnetmern toal e annhda enxctee trrnaanls sptaakreenhcoyld aenrds that detail</td><td>H Biuams aannd-A HIo Cmonofiggeunriazatitioonn; Harmful</td></tr><tr><td>MG-4.1-006</td><td>Track dataset modifications forprovenance by monitoring data deletions, rectification requests, and other changes that may impact the verifiability of content origins.</td><td>Information Integrity</td></tr></tbody></table>

<!-- page: 49 -->

<table><tbody><tr><td>MG-4.1-007</td><td>V e pveroarivlfueyan ttahena GcteA AIdI sa Aytcsattoe trrmascr pkeeisnrpfgoo trnemsciahbnnleciqe fou ierns mc,luo adnnidintog prrtiohnmeg r apeptplpyoli erctsaectidaol ianstse ouf ies cssou cneatnse fn eofftre rcetispveolnyse.</td><td>H Inufomrmana-tiAoIn Co Inntfieggurritaytion;</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Affected Individuals and Communities, Domain Experts, End-Users, Human Factors, Operation and Monitoring</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 4.2:Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI Actors.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-4.2-001</td><td>C peornfdourmcta rnecgeu,la fere mdobnacitko rreincgeiovfe Gd,A aIn sdys itmemprso avnedm peunbtslis mha rdeep.orts detailing the</td><td>Harmful Bias and Homogenization</td></tr><tr><td>MG-4.2-002</td><td>Practice and follow incident response plans for addressing the generation of inappropriate or harmful content and adapt processes based on findings to prevent future occurrences. Conduct post-mortem analyses of incidents with relevant AI Actors, to understand the root causes and implement preventive measures.</td><td>Human-AI Configuration; Dangerous, Violent, or Hateful Content</td></tr><tr><td>MG-4.2-003</td><td>U nosen- vteiscuhanliizcaatilo stnaske ohro oltdheerrs m unedtheorsdtsantodi rnegpr oefs GeAntI sGyAstIe mmo fduenlc btieohnaavliiotyr. to ease</td><td>Human-AI Configuration</td></tr><tr><td colspan="3">AI Actor Tasks: AI Deployment, AI Design, AI Development, Affected Individuals and Communities, End-Users, Operation and Monitoring, TEVV</td></tr></tbody></table>

<table><tbody><tr><td colspan="3">MANAGE 4.3:Incidents and errors are communicated to relevant AI Actors, including affected communities. Processes for tracking, responding to, and recovering from incidents and errors are followed and documented.</td></tr><tr><td>Action ID</td><td>Suggested Action</td><td>GAI Risks</td></tr><tr><td>MG-4.3-001</td><td>Conduct after-action assessments for GAI system incidents to verify incident r persopcoendsuere asn fdor re ccoomvemruyn pircoactiensgse insc aidreen fotsllo towe redle avnadnt eff AeIc Aticvtoer,s in acnludd winhge troe follow applicable, relevant legal and regulatory bodies.</td><td>Information Security</td></tr><tr><td>MG-4.3-002</td><td>E resptaobrltieshd a enrrdor ms,a ninetaari-nm pisosleicsie, asn adnd ne pgraoticevdeu imrepsa tcots r.ecord and track GAI system</td><td>C Inotnefgarbituylation;Information</td></tr></tbody></table>

<!-- page: 50 -->

<table><tbody><tr><td>MG-4.3-003</td><td>Report GAI incidents in compliance with legal and regulatory requirements (e.g., HIPAA breach reporting, e.g., OCR (2023) or NHTSA (2022) autonomous vehicle crash reporting requirements.</td><td>Information Security;Data Privacy</td></tr><tr><td colspan="3">AI Actor Tasks:AI Deployment, Affected Individuals and Communities, Domain Experts, End-Users, Human Factors, Operation and Monitoring</td></tr></tbody></table>

<!-- page: 51 -->

## Appendix A. Primary GAI Considerations

The following primary considerations were derived as overarching themes from the GAI PWG consultation process. These considerations (Governance, Pre-Deployment Testing, Content Provenance, and Incident Disclosure) are relevant for voluntary use by any organization designing, developing, and using GAI and also inform the Actions to Manage GAI risks. Information included about the primary considerations is not exhaustive, but highlights the most relevant topics derived from the GAI PWG.

Acknowledgments: These considerations could not have been surfaced without the helpful analysis and contributions from the community and NIST staff GAI PWG leads: George Awad, Luca Belli, Harold Booth, Mat Heyman, Yooyoung Lee, Mark Pryzbocki, Reva Schwartz, Martin Stanley, and Kyra Yee.

## A.1. Governance

## A.1.1. Overview

Like any other technology system, governance principles and techniques can be used to manage risks related to generative AI models, capabilities, and applications. Organizations may choose to apply their existing risk tiering to GAI systems, or they may opt to revise or update AI system risk levels to address these unique GAI risks. This section describes how organizational governance regimes may be reevaluated and adjusted for GAI contexts. It also addresses third-party considerations for governing across the AI value chain.

## A.1.2. Organizational Governance

GAI opportunities, risks and long-term performance characteristics are typically less well-understood than non-generative AI tools and may be perceived and acted upon by humans in ways that vary greatly. Accordingly, GAI may call for different levels of oversight from AI Actors or different human-AI configurations in order to manage their risks effectively. Organizations’ use of GAI systems may also warrant additional human review, tracking and documentation, and greater management oversight.

AI technology can produce varied outputs in multiple modalities and present many classes of user interfaces. This leads to a broader set of AI Actors interacting with GAI systems for widely differing applications and contexts of use. These can include data labeling and preparation, development of GAI models, content moderation, code generation and review, text generation and editing, image and video generation, summarization, search, and chat. These activities can take place within organizational settings or in the public domain.

Organizations can restrict AI applications that cause harm, exceed stated risk tolerances, or that conflict with their tolerances or values. Governance tools and protocols that are applied to other types of AI systems can be applied to GAI systems. These plans and actions include:

Accessibility and reasonable accommodations

• Auditing and assessment

• Change-management controls

• AI actor credentials and qualifications

Commercial use

• Alignment to organizational values

• Data provenance

<!-- page: 52 -->

Data protection

Data retention

Consistency in use of defining key terms

Decommissioning

• Discouraging anonymous use

Education

Impact assessments

Incident response

• Monitoring

• Opt-outs

• Risk-based controls

• Risk mapping and measurement

• Science-backed TEVV practices

• Secure software development practices

Stakeholder engagement

• Synthetic content detection and labeling tools and techniques

• Whistleblower protections

• Workforce diversity and interdisciplinary teams

Establishing acceptable use policies and guidance for the use of GAI in formal human-AI teaming settings as well as different levels of human-AI configurations can help to decrease risks arising from misuse, abuse, inappropriate repurpose, and misalignment between systems and users. These practices are just one example of adapting existing governance protocols for GAI contexts.

## A.1.3. Third-Party Considerations

Organizations may seek to acquire, embed, incorporate, or use open-source or proprietary third-party GAI models, systems, or generated data for various applications across an enterprise. Use of these GAI tools and inputs has implications for all functions of the organization – including but not limited to acquisition, human resources, legal, compliance, and IT services – regardless of whether they are carried out by employees or third parties. Many of the actions cited above are relevant and options for addressing third-party considerations.

Third party GAI integrations may give rise to increased intellectual property, data privacy, or information security risks, pointing to the need for clear guidelines for transparency and risk management regarding the collection and use of third-party data for model inputs. Organizations may consider varying risk controls for foundation models, fine-tuned models, and embedded tools, enhanced processes for interacting with external GAI technologies or service providers. Organizations can apply standard or existing risk controls and processes to proprietary or open-source GAI technologies, data, and third-party service providers, including acquisition and procurement due diligence, requests for software bills of materials (SBOMs), application of service level agreements (SLAs), and statement on standards for attestation engagement (SSAE) reports to help with third-party transparency and risk management for GAI systems.

## A.1.4. Pre-Deployment Testing

## Overview

The diverse ways and contexts in which GAI systems may be developed, used, and repurposed complicates risk mapping and pre-deployment measurement efforts. Robust test, evaluation, validation, and verification (TEVV) processes can be iteratively applied – and documented – in early stages of the AI lifecycle and informed by representative AI Actors [(see Figure 3 of the AI RMF)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf). Until new and rigorous

<!-- page: 53 -->

early lifecycle TEVV approaches are developed and matured for GAI, organizations may use recommended “pre-deployment testing” practices to measure performance, capabilities, limits, risks, and impacts. This section describes risk measurement and estimation as part of pre-deployment TEVV, and examines the state of play for pre-deployment testing methodologies.

## Limitations of Current Pre-deployment Test Approaches

Currently available pre-deployment TEVV processes used for GAI applications may be inadequate, non-systematically applied, or fail to reflect or mismatched to deployment contexts. For example, the anecdotal testing of GAI system capabilities through video games or standardized tests designed for humans (e.g., intelligence tests, professional licensing exams) does not guarantee GAI system validity or reliability in those domains. Similarly, jailbreaking or prompt engineering tests may not systematically assess validity or reliability risks.

Measurement gaps can arise from mismatches between laboratory and real-world settings. Current testing approaches often remain focused on laboratory conditions or restricted to benchmark test datasets and in silico techniques that may not extrapolate well to—or directly assess GAI impacts in real world conditions. For example, current measurement gaps for GAI make it difficult to precisely estimate its potential ecosystem-level or longitudinal risks and related political, social, and economic impacts. Gaps between benchmarks and real-world use of GAI systems may likely be exacerbated due to prompt sensitivity and broad heterogeneity of contexts of use.

## A.1.5. Structured Public Feedback

Structured public feedback can be used to evaluate whether GAI systems are performing as intended and to calibrate and verify traditional measurement methods. Examples of structured feedback include, but are not limited to:

**Participatory Engagement Methods**: Methods used to solicit feedback from civil society groups, affected communities, and users, including focus groups, small user studies, and surveys.

**Field Testing**: Methods used to determine how people interact with, consume, use, and make sense of AI-generated information, and subsequent actions and effects, including UX, usability, and other structured, randomized experiments.

**AI Red-teaming:** A [structured testing exercise](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/) used to probe an AI system to find flaws and vulnerabilities such as inaccurate, harmful, or discriminatory outputs, often in a controlled environment and in collaboration with system developers.

Information gathered from structured public feedback can inform design, implementation, deployment approval, maintenance, or decommissioning decisions. Results and insights gleaned from these exercises can serve multiple purposes, including improving data quality and preprocessing, bolstering governance decision making, and enhancing system documentation and debugging practices. When implementing feedback activities, organizations should follow human subjects research requirements and best practices such as informed consent and subject compensation.

<!-- page: 54 -->

## Participatory Engagement Methods

On an ad hoc or more structured basis, organizations can design and use a variety of channels to engage external stakeholders in product development or review. Focus groups with select experts can provide feedback on a range of issues. Small user studies can provide feedback from representative groups or populations. Anonymous surveys can be used to poll or gauge reactions to specific features. Participatory engagement methods are often less structured than field testing or red teaming, and are more commonly used in early stages of AI or product development.

## Field Testing

Field testing involves structured settings to evaluate risks and impacts and to simulate the conditions under which the GAI system will be deployed. Field style tests can be adapted from a focus on user preferences and experiences towards AI risks and impacts – both negative and positive. When carried out with large groups of users, these tests can provide estimations of the likelihood of risks and impacts in real world interactions.

Organizations may also collect feedback on outcomes, harms, and user experience directly from users in the production environment after a model has been released, in accordance with human subject standards such as informed consent and compensation. Organizations should follow applicable human subjects research requirements, and best practices such as informed consent and subject compensation, when implementing feedback activities.

## AI Red-teaming

AI red-teaming is an evolving practice that references exercises often conducted in a controlled environment and in collaboration with AI developers building AI models to identify potential adverse behavior or outcomes of a GAI model or system, how they could occur, and stress test safeguards”. AI red-teaming can be performed before or after AI models or systems are made available to the broader public; this section focuses on red-teaming in pre-deployment contexts.

The quality of AI red-teaming outputs is related to the background and expertise of the AI red team itself. Demographically and interdisciplinarily diverse AI red teams can be used to identify flaws in the varying contexts where GAI will be used. For best results, AI red teams should demonstrate domain expertise, and awareness of socio-cultural aspects within the deployment context. AI red-teaming results should be given additional analysis before they are incorporated into organizational governance and decision making, policy and procedural updates, and AI risk management efforts.

Various types of AI red-teaming may be appropriate, depending on the use case:

General Public: Performed by general users (not necessarily AI or technical experts) who are expected to use the model or interact with its outputs, and who bring their own lived experiences and perspectives to the task of AI red-teaming. These individuals may have been provided instructions and material to complete tasks which may elicit harmful model behaviors. This type of exercise can be more effective with large groups of AI red-teamers.

Expert: Performed by specialists with expertise in the domain or specific AI red-teaming context of use (e.g., medicine, biotech, cybersecurity).

Combination: In scenarios when it is difficult to identify and recruit specialists with sufficient domain and contextual expertise, AI red-teaming exercises may leverage both expert and

<!-- page: 55 -->

general public participants. For example, expert AI red-teamers could modify or verify the prompts written by general public AI red-teamers. These approaches may also expand coverage of the AI risk attack surface.

Human / AI: Performed by GAI in [combination with](https://arxiv.org/pdf/2401.15897) specialist or non-specialist human teams. GAI-led red-teaming can be more cost effective than human red-teamers alone. Human or GAI-led AI red-teaming may be better suited for eliciting different types of harms.

## A.1.6. Content Provenance

## Overview

GAI technologies can be leveraged for many applications such as content generation and synthetic data. Some aspects of GAI outputs, such as the production of deepfake content, can challenge our ability to distinguish human-generated content from AI-generated synthetic content. To help manage and mitigate these risks, digital transparency mechanisms like provenance data tracking can trace the origin and history of content. Provenance data tracking and synthetic content detection can help facilitate greater information access about both authentic and synthetic content to users, enabling better knowledge of trustworthiness in AI systems. When combined with other organizational accountability mechanisms, digital content transparency approaches can enable processes to trace negative outcomes back to their source, improve information integrity, and uphold public trust. Provenance data tracking and synthetic content detection mechanisms provide information about the [origin](https://www.itic.org/policy/ITI_AIContentAuthorizationPolicy_122123.pdf) and history of content to assist in GAI risk management efforts.

Provenance metadata can include information about GAI model developers or creators of GAI content, date/time of creation, location, modifications, and sources. Metadata can be tracked for text, images, videos, audio, and underlying datasets. The implementation of provenance data tracking techniques can help assess the authenticity, integrity, intellectual property rights, and potential manipulations in digital content. Some well-known techniques for provenance data tracking [include](https://www.semanticscholar.org/paper/Provable-Robust-Watermarking-for-AI-Generated-%20Text-Zhao-Ananth/e3ee09fb2bcc29e992cdcf0d0db6fcb6e5c56384) digital [watermarking,](https://openreview.net/forum?id=aX8ig9X2a7) metadata recording, digital fingerprinting, and human authentication, [among others.](https://partnershiponai.org/glossary-for-synthetic-media-transparency-methods-part-1-indirect-disclosure/)

## Provenance Data Tracking Approaches

Provenance data tracking techniques for GAI systems can be used to track the history and origin of data inputs, metadata, and synthetic content. Provenance data tracking records the origin and history for digital content, allowing its authenticity to be determined. It consists of techniques to record metadata as well as overt and covert digital watermarks on content. Data provenance refers to tracking the origin and history of input data through metadata and digital watermarking techniques. Provenance data tracking processes can include and assist AI Actors across the lifecycle who may not have full visibility or control over the various trade-offs and cascading impacts of early-stage model decisions on downstream performance and synthetic outputs. For example, by selecting a watermarking model to prioritize robustness (the durability of a watermark), an AI actor may inadvertently diminish [computational complexity](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7057071&tag=1) (the resources required to implement watermarking). Organizational risk management efforts for enhancing content provenance include:

Tracking provenance of training data and metadata for GAI systems;

Documenting provenance data limitations within GAI systems;

<!-- page: 56 -->

• Monitoring system capabilities and limitations in deployment through rigorous TEVV processes;

Evaluating how humans engage, interact with, or adapt to GAI content (especially in decision making tasks informed by GAI content), and how they react to applied provenance techniques such as overt disclosures.

Organizations can document and delineate GAI system objectives and limitations to identify gaps where provenance data may be most useful. For instance, GAI systems used for content creation may require robust watermarking techniques and corresponding detectors to identify the source of content or metadata recording techniques and metadata management tools and repositories to trace content origins and modifications. Further narrowing of GAI task definitions to include provenance data can enable organizations to maximize the utility of provenance data and risk management efforts.

## A.1.7. Enhancing Content Provenance through Structured Public Feedback

While indirect feedback methods such as automated error collection systems are useful, they often lack the [context and depth](https://arxiv.org/abs/2304.02819) that direct input from end users can provide. Organizations can leverage feedback approaches described in the <u>Pre-Deployment Testing section</u> to capture input from external sources such as through AI red-teaming.

Integrating pre- and post-deployment external feedback into the monitoring process for GAI models and corresponding applications can help enhance awareness of performance changes and mitigate potential risks and harms from outputs. There are many ways to capture and make use of user feedback – before and after GAI systems and digital content transparency approaches are deployed – to gain insights about authentication efficacy and vulnerabilities, impacts of adversarial threats on techniques, and unintended consequences resulting from the utilization of content provenance approaches on users and communities. Furthermore, organizations can track and document the provenance of datasets to identify instances in which AI-generated data is a potential root cause of performance issues with the GAI system.

## A.1.8. Incident Disclosure

## Overview

AI incidents can be [defined](https://oecd.ai/en/incidents-methodology) as an “event, circumstance, or series of events where the development, use, or malfunction of one or more AI systems directly or indirectly contributes to one of the following harms: injury or harm to the health of a person or groups of people (including psychological harms and harms to mental health); disruption of the management and operation of critical infrastructure; violations of human rights or a breach of obligations under applicable law intended to protect fundamental, labor, and intellectual property rights; or harm to property, communities, or the environment.” AI incidents can occur in the aggregate (i.e., for systemic discrimination) or acutely (i.e., for one individual).

## State of AI Incident Tracking and Disclosure

Formal channels do not currently exist to report and document AI incidents. However, a number of [publicly available databases](https://incidentdatabase.ai/) have been created to document their occurrence. These reporting channels make decisions on an ad hoc basis about what kinds of incidents to track. Some, for example, track by [amount of media coverage.](https://oecd.ai/en/incidents-methodology)

<!-- page: 57 -->

Documenting, reporting, and sharing information about GAI incidents can help mitigate and prevent harmful outcomes by assisting relevant AI Actors in [tracing impacts to their source.](https://dl.acm.org/doi/fullHtml/10.1145/3600211.3604700) Greater awareness and standardization of GAI incident reporting could promote this transparency and improve GAI risk management across the AI ecosystem.

## Documentation and Involvement of AI Actors

AI Actors should be aware of their roles in reporting AI incidents. To better understand previous incidents and implement measures to prevent similar ones in the future, organizations could consider developing guidelines for publicly available incident reporting which include information about AI actor responsibilities. These guidelines would help AI system operators identify GAI incidents across the AI lifecycle and with AI Actors regardless of role. Documentation and review of third-party inputs and plugins for GAI systems is especially important for AI Actors in the context of incident disclosure; LLM inputs and content delivered through these [plugins is often distributed,](https://owasp.org/www-project-top-10-for-large-language-model-applications/) with inconsistent or insufficient access control.

Documentation practices including logging, recording, and analyzing GAI incidents can facilitate smoother sharing of information with relevant AI Actors. Regular information sharing, change management records, version history and metadata can also empower AI Actors responding to and managing AI incidents.

<!-- page: 58 -->

## Appendix B. References

Acemoglu, D. (2024) The Simple Macroeconomics of AI [https://www.nber.org/papers/w32487](https://www.nber.org/papers/w32487)

AI Incident Database. [https://incidentdatabase.ai/](https://incidentdatabase.ai/)

Atherton, D. (2024) Deepfakes and Child Safety: A Survey and Analysis of 2023 Incidents and Responses. AI Incident Database. [https://incidentdatabase.ai/blog/deepfakes-and-child-safety/](https://incidentdatabase.ai/blog/deepfakes-and-child-safety/)

Badyal, N. et al. (2023) Intentional Biases in LLM Responses. arXiv. [https://arxiv.org/pdf/2311.07611](https://arxiv.org/pdf/2311.07611)

Bing Chat: Data Exfiltration Exploit Explained. Embrace The Red. [https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/](https://embracethered.com/blog/posts/2023/bing-chat-data-exfiltration-poc-and-fix/)

Bommasani, R. et al. (2022) Picking on the Same Person: Does Algorithmic Monoculture lead to Outcome Homogenization? arXiv. [https://arxiv.org/pdf/2211.13972](https://arxiv.org/pdf/2211.13972)

Boyarskaya, M. et al. (2020) Overcoming Failures of Imagination in AI Infused System Development and Deployment. arXiv. [https://arxiv.org/pdf/2011.13416](https://arxiv.org/pdf/2011.13416)

Browne, D. et al. (2023) Securing the AI Pipeline. Mandiant. [https://www.mandiant.com/resources/blog/securing-ai-pipeline](https://www.mandiant.com/resources/blog/securing-ai-pipeline)

Burgess, M. (2024) Generative AI’s Biggest Security Flaw Is Not Easy to Fix. WIRED. [https://www.wired.com/story/generative-ai-prompt-injection-hacking/](https://www.wired.com/story/generative-ai-prompt-injection-hacking/)

Burtell, M. et al. (2024) The Surprising Power of Next Word Prediction: Large Language Models Explained, Part 1. Georgetown Center for Security and Emerging Technology. [https://cset.georgetown.edu/article/the-surprising-power-of-next-word-prediction-large-language-models-explained-part-1/](https://cset.georgetown.edu/article/the-surprising-power-of-next-word-prediction-large-language-models-explained-part-1/)

Canadian Centre for Cyber Security (2023) Generative artificial intelligence (AI) - ITSAP.00.041. [https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041](https://www.cyber.gc.ca/en/guidance/generative-artificial-intelligence-ai-itsap00041)

Carlini, N., et al. (2021) Extracting Training Data from Large Language Models. Usenix. [https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting](https://www.usenix.org/conference/usenixsecurity21/presentation/carlini-extracting)

Carlini, N. et al. (2023) Quantifying Memorization Across Neural Language Models. ICLR 2023. [https://arxiv.org/pdf/2202.07646](https://arxiv.org/pdf/2202.07646)

Carlini, N. et al. (2024) Stealing Part of a Production Language Model. arXiv. [https://arxiv.org/abs/2403.06634](https://arxiv.org/abs/2403.06634)

Chandra, B. et al. (2023) Dismantling the Disinformation Business of Chinese Influence Operations. RAND. [https://www.rand.org/pubs/commentary/2023/10/dismantling-the-disinformation-business-of-chinese.html](https://www.rand.org/pubs/commentary/2023/10/dismantling-the-disinformation-business-of-chinese.html)

Ciriello, R. et al. (2024) Ethical Tensions in Human-AI Companionship: A Dialectical Inquiry into Replika. ResearchGate. [https://www.researchgate.net/publication/374505266\_Ethical\_Tensions\_in\_Human-AI\_Companionship\_A\_Dialectical\_Inquiry\_into\_Replika](https://www.researchgate.net/publication/374505266_Ethical_Tensions_in_Human-AI_Companionship_A_Dialectical_Inquiry_into_Replika)

Dahl, M. et al. (2024) Large Legal Fictions: Profiling Legal Hallucinations in Large Language Models. arXiv. [https://arxiv.org/abs/2401.01301](https://arxiv.org/abs/2401.01301)

<!-- page: 59 -->

De Angelo, D. (2024) Short, Mid and Long-Term Impacts of AI in Cybersecurity. Palo Alto Networks. [https://www.paloaltonetworks.com/blog/2024/02/impacts-of-ai-in-cybersecurity/](https://www.paloaltonetworks.com/blog/2024/02/impacts-of-ai-in-cybersecurity/)

De Freitas, J. et al. (2023) Chatbots and Mental Health: Insights into the Safety of Generative AI. Harvard Business School. [https://www.hbs.edu/ris/Publication%20Files/23-011\_c1bdd417-f717-47b6-bccb-5438c6e65c1a\_f6fd9798-3c2d-4932-b222-056231fe69d7.pdf](https://www.hbs.edu/ris/Publication%20Files/23-011_c1bdd417-f717-47b6-bccb-5438c6e65c1a_f6fd9798-3c2d-4932-b222-056231fe69d7.pdf)

Dietvorst, B. et al. (2014) Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err. Journal of Experimental Psychology. [https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf](https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf)

Duhigg, C. (2012) How Companies Learn Your Secrets. New York Times. [https://www.nytimes.com/2012/02/19/magazine/shopping-habits.html](https://www.nytimes.com/2012/02/19/magazine/shopping-habits.html)

Elsayed, G. et al. (2024) Images altered to trick machine vision can influence humans too. Google DeepMind. [https://deepmind.google/discover/blog/images-altered-to-trick-machine-vision-can-influence-humans-too/](https://deepmind.google/discover/blog/images-altered-to-trick-machine-vision-can-influence-humans-too/)

Epstein, Z. et al. (2023). Art and the science of generative AI. Science. [https://www.science.org/doi/10.1126/science.adh4451](https://www.science.org/doi/10.1126/science.adh4451)

Feffer, M. et al. (2024) Red-Teaming for Generative AI: Silver Bullet or Security Theater? arXiv. [https://arxiv.org/pdf/2401.15897](https://arxiv.org/pdf/2401.15897)

Glazunov, S. et al. (2024) Project Naptime: Evaluating Offensive Security Capabilities of Large Language Models. Project Zero. [https://googleprojectzero.blogspot.com/2024/06/project-naptime.html](https://googleprojectzero.blogspot.com/2024/06/project-naptime.html)

Greshake, K. et al. (2023) Not what you've signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. arXiv. [https://arxiv.org/abs/2302.12173](https://arxiv.org/abs/2302.12173)

Hagan, M. (2024) Good AI Legal Help, Bad AI Legal Help: Establishing quality standards for responses to people’s legal problem stories. SSRN. [https://papers.ssrn.com/sol3/papers.cfm?abstract\_id=4696936](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4696936)

Haran, R. (2023) Securing LLM Systems Against Prompt Injection. NVIDIA. [https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/](https://developer.nvidia.com/blog/securing-llm-systems-against-prompt-injection/)

Information Technology Industry Council (2024) Authenticating AI-Generated Content. [https://www.itic.org/policy/ITI\_AIContentAuthorizationPolicy\_122123.pdf](https://www.itic.org/policy/ITI_AIContentAuthorizationPolicy_122123.pdf)

Jain, S. et al. (2023) Algorithmic Pluralism: A Structural Approach To Equal Opportunity. arXiv. [https://arxiv.org/pdf/2305.08157](https://arxiv.org/pdf/2305.08157)

Ji, Z. et al (2023) Survey of Hallucination in Natural Language Generation. ACM Comput. Surv. 55, 12, Article 248. [https://doi.org/10.1145/3571730](https://doi.org/10.1145/3571730)

Jones-Jang, S. et al. (2022) How do people react to AI failure? Automation bias, algorithmic aversion, and perceived controllability. Oxford. [https://academic.oup.com/jcmc/article/28/1/zmac029/6827859\]](https://academic.oup.com/jcmc/article/28/1/zmac029/6827859)

Jussupow, E. et al. (2020) Why Are We Averse Towards Algorithms? A Comprehensive Literature Review on Algorithm Aversion. ECIS 2020. [https://aisel.aisnet.org/ecis2020\_rp/168/](https://aisel.aisnet.org/ecis2020_rp/168/)

Kalai, A., et al. (2024) Calibrated Language Models Must Hallucinate. arXiv. [https://arxiv.org/pdf/2311.14648](https://arxiv.org/pdf/2311.14648)

<!-- page: 60 -->

Karasavva, V. et al. (2021) Personality, Attitudinal, and Demographic Predictors of Non-consensual Dissemination of Intimate Images. NIH. [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9554400/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9554400/)

Katzman, J., et al. (2023) Taxonomizing and measuring representational harms: a look at image tagging. AAAI. [https://dl.acm.org/doi/10.1609/aaai.v37i12.26670](https://dl.acm.org/doi/10.1609/aaai.v37i12.26670)

Khan, T. et al. (2024) From Code to Consumer: PAI’s Value Chain Analysis Illuminates Generative AI’s Key Players. AI. [https://partnershiponai.org/from-code-to-consumer-pais-value-chain-analysis-illuminates-generative-ais-key-players/](https://partnershiponai.org/from-code-to-consumer-pais-value-chain-analysis-illuminates-generative-ais-key-players/)

Kirchenbauer, J. et al. (2023) A Watermark for Large Language Models. OpenReview. [https://openreview.net/forum?id=aX8ig9X2a7](https://openreview.net/forum?id=aX8ig9X2a7)

Kleinberg, J. et al. (May 2021) Algorithmic monoculture and social welfare. PNAS. [https://www.pnas.org/doi/10.1073/pnas.2018340118](https://www.pnas.org/doi/10.1073/pnas.2018340118)

Lakatos, S. (2023) A Revealing Picture. Graphika. [https://graphika.com/reports/a-revealing-picture](https://graphika.com/reports/a-revealing-picture)

Lee, H. et al. (2024) Deepfakes, Phrenology, Surveillance, and More! A Taxonomy of AI Privacy Risks. arXiv. [https://arxiv.org/pdf/2310.07879](https://arxiv.org/pdf/2310.07879)

Lenaerts-Bergmans, B. (2024) Data Poisoning: The Exploitation of Generative AI. Crowdstrike. [https://www.crowdstrike.com/cybersecurity-101/cyberattacks/data-poisoning/](https://www.crowdstrike.com/cybersecurity-101/cyberattacks/data-poisoning/)

Liang, W. et al. (2023) GPT detectors are biased against non-native English writers. arXiv. [https://arxiv.org/abs/2304.02819](https://arxiv.org/abs/2304.02819)

Luccioni, A. et al. (2023) Power Hungry Processing: Watts Driving the Cost of AI Deployment? arXiv. [https://arxiv.org/pdf/2311.16863](https://arxiv.org/pdf/2311.16863)

Mouton, C. et al. (2024) The Operational Risks of AI in Large-Scale Biological Attacks. RAND. [https://www.rand.org/pubs/research\_reports/RRA2977-2.html.](https://www.rand.org/pubs/research_reports/RRA2977-2.html)

Nicoletti, L. et al. (2023) Humans Are Biased. Generative Ai Is Even Worse. Bloomberg. [https://www.bloomberg.com/graphics/2023-generative-ai-bias/.](https://www.bloomberg.com/graphics/2023-generative-ai-bias/)

National Institute of Standards and Technology (2024) Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations [https://csrc.nist.gov/pubs/ai/100/2/e2023/final](https://csrc.nist.gov/pubs/ai/100/2/e2023/final)

National Institute of Standards and Technology (2023) AI Risk Management Framework. [https://www.nist.gov/itl/ai-risk-management-framework](https://www.nist.gov/itl/ai-risk-management-framework)

National Institute of Standards and Technology (2023) AI Risk Management Framework, Chapter 3: AI Risks and Trustworthiness. [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/AI\_RMF/Foundational\_Information/3-sec-characteristics](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Foundational_Information/3-sec-characteristics)

National Institute of Standards and Technology (2023) AI Risk Management Framework, Chapter 6: AI RMF Profiles. [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/AI\_RMF/Core\_And\_Profiles/6-sec-profile](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Core_And_Profiles/6-sec-profile)

National Institute of Standards and Technology (2023) AI Risk Management Framework, Appendix A: Descriptions of AI Actor Tasks. [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/AI\_RMF/Appendices/Appendix\_A#:\~:text=AI%20actors%20in%20this%20category,data%20providers%2C%20system%20funders%2C%20product](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Appendices/Appendix_A#:%7E:text=AI%20actors%20in%20this%20category,data%20providers%2C%20system%20funders%2C%20product)

<!-- page: 61 -->

OpenAI (2023) GPT-4 System Card. [https://cdn.openai.com/papers/gpt-4-system-card.pdf](https://cdn.openai.com/papers/gpt-4-system-card.pdf)OpenAI (2024) GPT-4 Technical Report. [https://arxiv.org/pdf/2303.08774](https://arxiv.org/pdf/2303.08774)

National Institute of Standards and Technology (2023) AI Risk Management Framework, Appendix B: How AI Risks Differ from Traditional Software Risks. [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/AI\_RMF/Appendices/Appendix\_B](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Appendices/Appendix_B)

National Institute of Standards and Technology (2023) AI RMF Playbook. [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/Playbook](https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook)

National Institue of Standards and Technology (2023) Framing Risk [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/AI\_RMF/Foundational\_Information/1-sec-risk](https://airc.nist.gov/AI_RMF_Knowledge_Base/AI_RMF/Foundational_Information/1-sec-risk)

National Institute of Standards and Technology (2023) The Language of Trustworthy AI: An In-Depth Glossary of Terms [https://airc.nist.gov/AI\_RMF\_Knowledge\_Base/Glossary](https://airc.nist.gov/AI_RMF_Knowledge_Base/Glossary)

National Institue of Standards and Technology (2022) Towards a Standard for Identifying and Managing Bias in Artificial Intelligence [https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence](https://www.nist.gov/publications/towards-standard-identifying-and-managing-bias-artificial-intelligence)

Northcutt, C. et al. (2021) Pervasive Label Errors in Test Sets Destabilize Machine Learning Benchmarks. arXiv. [https://arxiv.org/pdf/2103.14749](https://arxiv.org/pdf/2103.14749)

OECD (2023) "Advancing accountability in AI: Governing and managing risks throughout the lifecycle for trustworthy AI", OECD Digital Economy Papers, No. 349, OECD Publishing, Paris. [https://doi.org/10.1787/2448f04b-en](https://doi.org/10.1787/2448f04b-en)

OECD (2024) "Defining AI incidents and related terms" OECD Artificial Intelligence Papers, No. 16, OECD Publishing, Paris. [https://doi.org/10.1787/d1a8d965-en](https://doi.org/10.1787/d1a8d965-en)

Padmakumar, V. et al. (2024) Does writing with language models reduce content diversity? ICLR. [https://arxiv.org/pdf/2309.05196](https://arxiv.org/pdf/2309.05196)

Park, P. et. al. (2024) AI deception: A survey of examples, risks, and potential solutions. Patterns, 5(5). arXiv. [https://arxiv.org/pdf/2308.14752](https://arxiv.org/pdf/2308.14752)

Partnership on AI (2023) Building a Glossary for Synthetic Media Transparency Methods, Part 1: Indirect Disclosure. [https://partnershiponai.org/glossary-for-synthetic-media-transparency-methods-part-1-indirect-disclosure/](https://partnershiponai.org/glossary-for-synthetic-media-transparency-methods-part-1-indirect-disclosure/)

Qu, Y. et al. (2023) Unsafe Diffusion: On the Generation of Unsafe Images and Hateful Memes From Text-To-Image Models. arXiv. [https://arxiv.org/pdf/2305.13873](https://arxiv.org/pdf/2305.13873)

Rafat, K. et al. (2023) Mitigating carbon footprint for knowledge distillation based deep learning model compression. PLOS One. [https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0285668](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0285668)

Said, I. et al. (2022) Nonconsensual Distribution of Intimate Images: Exploring the Role of Legal Attitudes in Victimization and Perpetration. Sage. [https://journals.sagepub.com/doi/full/10.1177/08862605221122834#bibr47-08862605221122834](https://journals.sagepub.com/doi/full/10.1177/08862605221122834#bibr47-08862605221122834)

Sandbrink, J. (2023) Artificial intelligence and biological misuse: Differentiating risks of language models and biological design tools. arXiv. [https://arxiv.org/pdf/2306.13952](https://arxiv.org/pdf/2306.13952)

<!-- page: 62 -->

Satariano, A. et al. (2023) The People Onscreen Are Fake. The Disinformation Is Real. New York Times. [https://www.nytimes.com/2023/02/07/technology/artificial-intelligence-training-deepfake.html](https://www.nytimes.com/2023/02/07/technology/artificial-intelligence-training-deepfake.html)

Schaul, K. et al. (2024) Inside the secret list of websites that make AI like ChatGPT sound smart. Washington Post. [https://www.washingtonpost.com/technology/interactive/2023/ai-chatbot-learning/](https://www.washingtonpost.com/technology/interactive/2023/ai-chatbot-learning/)

Scheurer, J. et al. (2023) Technical report: Large language models can strategically deceive their users when put under pressure. arXiv. https://arxiv.org/abs/2311.07590

Shelby, R. et al. (2023) Sociotechnical Harms of Algorithmic Systems: Scoping a Taxonomy for Harm Reduction. arXiv. [https://arxiv.org/pdf/2210.05791](https://arxiv.org/pdf/2210.05791)

Shevlane, T. et al. (2023) Model evaluation for extreme risks. arXiv. [https://arxiv.org/pdf/2305.15324](https://arxiv.org/pdf/2305.15324)

Shumailov, I. et al. (2023) The curse of recursion: training on generated data makes models forget. arXiv. [https://arxiv.org/pdf/2305.17493v2](https://arxiv.org/pdf/2305.17493v2)

Smith, A. et al. (2023) Hallucination or Confabulation? Neuroanatomy as metaphor in Large Language Models. PLOS Digital Health. [https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000388](https://journals.plos.org/digitalhealth/article?id=10.1371/journal.pdig.0000388)

Soice, E. et al. (2023) Can large language models democratize access to dual-use biotechnology? arXiv. [https://arxiv.org/abs/2306.03809](https://arxiv.org/abs/2306.03809)

Solaiman, I. et al. (2023) The Gradient of Generative AI Release: Methods and Considerations. arXiv. [https://arxiv.org/abs/2302.04844](https://arxiv.org/abs/2302.04844)

Staab, R. et al. (2023) Beyond Memorization: Violating Privacy via Inference With Large Language Models. arXiv. [https://arxiv.org/pdf/2310.07298](https://arxiv.org/pdf/2310.07298)

Stanford, S. et al. (2023) Whose Opinions Do Language Models Reflect? arXiv. [https://arxiv.org/pdf/2303.17548](https://arxiv.org/pdf/2303.17548)

Strubell, E. et al. (2019) Energy and Policy Considerations for Deep Learning in NLP. arXiv. [https://arxiv.org/pdf/1906.02243](https://arxiv.org/pdf/1906.02243)

The White House (2016) Circular No. A-130, Managing Information as a Strategic Resource. [https://www.whitehouse.gov/wp-content/uploads/legacy\_drupal\_files/omb/circulars/A130/a130revised.pdf](https://www.whitehouse.gov/wp-content/uploads/legacy_drupal_files/omb/circulars/A130/a130revised.pdf)

The White House (2023) Executive Order on the Safe, Secure, and Trustworthy Development and Use of Artificial Intelligence. [https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/](https://www.whitehouse.gov/briefing-room/presidential-actions/2023/10/30/executive-order-on-the-safe-secure-and-trustworthy-development-and-use-of-artificial-intelligence/)

The White House (2022) Roadmap for Researchers on Priorities Related to Information Integrity Research and Development. [https://www.whitehouse.gov/wp-content/uploads/2022/12/Roadmap-Information-Integrity-RD-2022.pdf?](https://www.whitehouse.gov/wp-content/uploads/2022/12/Roadmap-Information-Integrity-RD-2022.pdf?)

Thiel, D. (2023) Investigation Finds AI Image Generation Models Trained on Child Abuse. Stanford Cyber Policy Center. [https://cyber.fsi.stanford.edu/news/investigation-finds-ai-image-generation-models-trained-child-abuse](https://cyber.fsi.stanford.edu/news/investigation-finds-ai-image-generation-models-trained-child-abuse)

<!-- page: 63 -->

Tirrell, L. (2017) Toxic Speech: Toward an Epidemiology of Discursive Harm. Philosophical Topics, 45(2), 139-162. [https://www.jstor.org/stable/26529441](https://www.jstor.org/stable/26529441)

Tufekci, Z. (2015) Algorithmic Harms Beyond Facebook and Google: Emergent Challenges of Computational Agency. Colorado Technology Law Journal. [https://ctlj.colorado.edu/wp-content/uploads/2015/08/Tufekci-final.pdf](https://ctlj.colorado.edu/wp-content/uploads/2015/08/Tufekci-final.pdf)

Turri, V. et al. (2023) Why We Need to Know More: Exploring the State of AI Incident Documentation Practices. AAAI/ACM Conference on AI, Ethics, and Society. [https://dl.acm.org/doi/fullHtml/10.1145/3600211.3604700](https://dl.acm.org/doi/fullHtml/10.1145/3600211.3604700)

Urbina, F. et al. (2022) Dual use of artificial-intelligence-powered drug discovery. Nature Machine Intelligence. [https://www.nature.com/articles/s42256-022-00465-9](https://www.nature.com/articles/s42256-022-00465-9)

Wang, X. et al. (2023) Energy and Carbon Considerations of Fine-Tuning BERT. ACL Anthology. [https://aclanthology.org/2023.findings-emnlp.607.pdf](https://aclanthology.org/2023.findings-emnlp.607.pdf)

Wang, Y. et al. (2023) Do-Not-Answer: A Dataset for Evaluating Safeguards in LLMs. arXiv. [https://arxiv.org/pdf/2308.13387](https://arxiv.org/pdf/2308.13387)

Wardle, C. et al. (2017) Information Disorder: Toward an interdisciplinary framework for research and policy making. Council of Europe. [https://rm.coe.int/information-disorder-toward-an-interdisciplinary-framework-for-researc/168076277c](https://rm.coe.int/information-disorder-toward-an-interdisciplinary-framework-for-researc/168076277c)

Weatherbed, J. (2024) Trolls have flooded X with graphic Taylor Swift AI fakes. The Verge. [https://www.theverge.com/2024/1/25/24050334/x-twitter-taylor-swift-ai-fake-images-trending](https://www.theverge.com/2024/1/25/24050334/x-twitter-taylor-swift-ai-fake-images-trending)

Wei, J. et al. (2024) Long Form Factuality in Large Language Models. arXiv. [https://arxiv.org/pdf/2403.18802](https://arxiv.org/pdf/2403.18802)

Weidinger, L. et al. (2021) Ethical and social risks of harm from Language Models. arXiv. [https://arxiv.org/pdf/2112.04359](https://arxiv.org/pdf/2112.04359)

Weidinger, L. et al. (2023) Sociotechnical Safety Evaluation of Generative AI Systems. arXiv. [https://arxiv.org/pdf/2310.11986](https://arxiv.org/pdf/2310.11986)

Weidinger, L. et al. (2022) Taxonomy of Risks posed by Language Models. FAccT ’22. [https://dl.acm.org/doi/pdf/10.1145/3531146.3533088](https://dl.acm.org/doi/pdf/10.1145/3531146.3533088)

West, D. (2023) AI poses disproportionate risks to women. Brookings. [https://www.brookings.edu/articles/ai-poses-disproportionate-risks-to-women/](https://www.brookings.edu/articles/ai-poses-disproportionate-risks-to-women/)

Wu, K. et al. (2024) How well do LLMs cite relevant medical references? An evaluation framework and analyses. arXiv. [https://arxiv.org/pdf/2402.02008](https://arxiv.org/pdf/2402.02008)

Yin, L. et al. (2024) OpenAI’s GPT Is A Recruiter’s Dream Tool. Tests Show There’s Racial Bias. Bloomberg. [https://www.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/](https://www.bloomberg.com/graphics/2024-openai-gpt-hiring-racial-discrimination/)

Yu, Z. et al. (March 2024) Don’t Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models. arXiv. [https://arxiv.org/html/2403.17336v1](https://arxiv.org/html/2403.17336v1)

Zaugg, I. et al. (2022) Digitally-disadvantaged languages. Policy Review. [https://policyreview.info/pdf/policyreview-2022-2-1654.pdf](https://policyreview.info/pdf/policyreview-2022-2-1654.pdf)

<!-- page: 64 -->

Zhang, Y. et al. (2023) Human favoritism, not AI aversion: People’s perceptions (and bias) toward generative AI, human experts, and human–GAI collaboration in persuasive content generation. Judgment and Decision Making. [https://www.cambridge.org/core/journals/judgment-and-decision-making/article/human-favoritism-not-ai-aversion-peoples-perceptions-and-bias-toward-generative-ai-human-experts-and-humangai-collaboration-in-persuasive-content-generation/419C4BD9CE82673EAF1D8F6C350C4FA8](https://www.cambridge.org/core/journals/judgment-and-decision-making/article/human-favoritism-not-ai-aversion-peoples-perceptions-and-bias-toward-generative-ai-human-experts-and-humangai-collaboration-in-persuasive-content-generation/419C4BD9CE82673EAF1D8F6C350C4FA8)

Zhang, Y. et al. (2023) Siren’s Song in the AI Ocean: A Survey on Hallucination in Large Language Models. arXiv. [https://arxiv.org/pdf/2309.01219](https://arxiv.org/pdf/2309.01219)

Zhao, X. et al. (2023) Provable Robust Watermarking for AI-Generated Text. Semantic Scholar. [https://www.semanticscholar.org/paper/Provable-Robust-Watermarking-for-AI-Generated-Text-Zhao-Ananth/75b68d0903af9d9f6e47ce3cf7e1a7d27ec811dc](https://www.semanticscholar.org/paper/Provable-Robust-Watermarking-for-AI-Generated-Text-Zhao-Ananth/75b68d0903af9d9f6e47ce3cf7e1a7d27ec811dc)
