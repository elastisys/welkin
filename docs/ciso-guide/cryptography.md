---
tags:
  #- ISO 27001:2013 A.10.1.2 Key Management
  - HSLF-FS 2016:40 3 kap. 15 § Behandling av personuppgifter i öppna nät
  - ISO 27001 Annex A 8.24 Use of Cryptography
---

# Cryptography Dashboard

## Relevant Regulations

### GDPR

[GDPR Article 32](https://gdpr.fan/a32):

> Taking into account the state of the art [...] the controller and the processor shall implement [...] as appropriate [...] encryption of personal data;
>
> In assessing the appropriate level of security account shall be taken in particular of the risks that are presented by processing, in particular from accidental or unlawful destruction, loss, alteration, **unauthorised disclosure of, or access to personal data transmitted**, stored or otherwise processed. [highlights added]

### Swedish Patient Data Law

!!!note

    This regulation is only available in Swedish. To avoid confusion, we decided not to produce an unofficial translation.

[HSLF-FS 2016:40](https://www.socialstyrelsen.se/globalassets/sharepoint-dokument/artikelkatalog/foreskrifter-och-allmanna-rad/2016-4-44.pdf):

<!-- vale off -->
> **Behandling av personuppgifter i öppna nät**
>
> 15 § Om vårdgivaren använder öppna nät vid behandling av personuppgifter, ska denne ansvara för att
>
> 1. överföring av uppgifterna görs på ett sådant sätt att inte obehöriga kan ta del av dem, och
> 1. elektronisk åtkomst eller direktåtkomst till uppgifterna föregås av stark autentisering.
<!-- vale on -->

## Mapping to ISO 27001 Controls

- [A.10.1.2 Key Management](https://www.isms.online/iso-27001/annex-a-10-cryptography/)

## Welkin Cryptography Dashboard

![Cryptography Dashboard](img/cryptography.png)

The Welkin Cryptography Dashboard allows to quickly audit the status of cryptography. It shows, amongst others, the public Internet endpoints (Ingresses) that are encrypted and the expiry time. Default Welkin configurations automatically renew certificates before expiry.

## Handling Non-Compliance

In case there is a violation of cryptography policies:

- If a certificate is expired and was not renewed, ask the administrator to check the status of `cert-manager` and `ingress-controller` component.
- If an endpoint is not encrypted, ask the developers to set the necessary [Ingress annotations](https://cert-manager.io/docs/usage/ingress/).
