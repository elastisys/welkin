---
search:
  boost: 2
tags:
  - BSI IT-Grundschutz APP.4.4.A13
---

# Guardrails

!!!important

    In 2021-01-27, the French Data Protection Authority (CNIL) imposed a fine on both the data controller and the data processor for failing to comply with their security obligations. For details, please read [this article](https://www.fieldfisher.com/en/services/privacy-security-and-information/privacy-security-and-information-law-blog/cnil-fines-controller-and-processor-for-security-v).

    Some of these guardrails might be "inconvenient" and "easy to disable". Faced with tight deadlines, it might be tempting to pressure administrators to disable some of these guardrails.

    **Prefer to keep these guardrails to avoid costly fines.** A guardrail should only be disabled if a risk assessment determined that the cost of implementation outweighs the risk to personal data.

<!-- vale off -->
> "Det ska vara lätt att göra rätt." (English: "It should be easy to do it right.")
<!-- vale on -->

We know you care about the security and uptime of your application. But all that effort goes wasted if the platform allows you to make trivial mistakes.

That is why Welkin is built with various guardrails. These are safeguards which allow you to make security and reliability easy for you.
Please look through the different pages in this Guardrails section to make yourself familiar with what the guardrails expect from your application.

## Relevant Regulations

- [GDPR Article 32](https://gdpr.fan/a32):

  > Taking into account the state of the art [...] the controller and the processor shall implement [...] as appropriate [...] a process for regularly testing, assessing and evaluating the effectiveness of technical and organisational measures for ensuring the security of the processing.
  >
  > In assessing the appropriate level of security account shall be taken in particular of the risks that are presented by processing, in particular from accidental or unlawful destruction, loss, alteration, **unauthorised disclosure of, or access to personal data transmitted**, stored or otherwise processed. [highlights added]

## Further Reading

- [Introduction to Guardrails and Paved Paths](https://www.daytona.io/dotfiles/introduction-to-guardrails-and-paved-paths).
