# Reporting security issues

If you think you have found a security vulnerability, please send a report to [security@elastisys.com](mailto:security@elastisys.com).

Please encrypt your message to us; please use our PGP key. The key fingerprint is:

`31AA7FFF035F50788C01294B6F878E4273E4D4B9`

The key is available from [keyserver.ubuntu.com](https://keyserver.ubuntu.com/pks/lookup?search=0x31AA7FFF035F50788C01294B6F878E4273E4D4B9&fingerprint=on&op=index).

**Important:** We ask you to not disclose the vulnerability before it has been fixed and announced, unless you received a response from the Elastisys security team that you can do so.

## Security patches

To receive notification when we release security patches, watch the [Releases](https://github.com/elastisys/compliantkubernetes-apps/releases) of this GitHub repository.

## Annex: sending encrypted messages

If you're not familiar with PGP here's a short step-by-step guide on how to send encrypted messages:

### 1. Import the recipient's public key

    gpg --keyserver keyserver.ubuntu.com --recv-keys 31AA7FFF035F50788C01294B6F878E4273E4D4B9

### 2. Encrypt your message

    gpg --encrypt --armor --recipient 31AA7FFF035F50788C01294B6F878E4273E4D4B9 --output message.txt.asc

Type your message, then press `Ctrl+D` when done.

_Alternatively_, if you've already got a message in a file called `message.txt`:

    gpg --encrypt --armor --recipient 31AA7FFF035F50788C01294B6F878E4273E4D4B9 message.txt

This creates a new file called `message.txt.asc` with your encrypted message.

### 3. Send it

Copy the entire encrypted output from the file (including the `-----BEGIN PGP MESSAGE-----` and `-----END PGP MESSAGE-----` lines) and paste it as your email body. Send your email to [security@elastisys.com](mailto:security@elastisys.com).
