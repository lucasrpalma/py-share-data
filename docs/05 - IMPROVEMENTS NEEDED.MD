# Improvements needed
The exercise was made considering solely the scope of data sharing differently according to the role.

For a much stronger security overall, it would need a lot more security controls and quality checks, as for example:
- Communication over TLS protocol
- Better authentication, as:
  - Strong authentication protocol implementation (like OAUTH2)
  - Better token management (incuding expiration)
  - Better cryptographic algorithms (maybe PBKDF2 instead of SHA512)
- More user management features, as:
  - User registration
  - Password recovery
  - Change password
  - MFA
  - Check for weak password
- Protection against brute force, as:
  - Block the user and/or the IP after a few tries
  - Throttling on the requests
- Requests through Firewall and WAF
- CI/CD with SAST, SCA, DAST and other security tools
- Better logging (including using **logging** instead of **print**)
- Docker image hardening
- External secrets service usage instead of hardcoded passwords
- Check for long inputs trying to make a DoS
- Better testing against concurrency issues
- Better error handling
- Unit and integrations tests