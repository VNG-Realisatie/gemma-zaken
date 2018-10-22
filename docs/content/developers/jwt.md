# JWT vs. OAUTH

* JWT is a type of token vs.

* OAUTH is framework how to dispense tokens

> Often people think "OAuth token" always implies an opaque token that is
  granted by a OAuth token dispensary, that can then be validated only by that
  same OAuth dispensary system. But this is not the only kind of OAuth token.
  JWT is just a different kind of OAuth token.

Geen OAUTH -> no need to contact the provider of the (opaque) token. Also not
needed if using JWT with OAUTH. Then what's the benefit of OAUTH?

https://community.apigee.com/questions/21139/jwt-vs-oauth.html

What are the places you'd want to use opaque tokens versus JWT?

## Use JWT when...

* Federation is desired. For example, you want to use Azure AD as the token
  issuer, and then use Apigee Edge as the token validator. With JWT, an app can
  authenticate to Azure AD, receive a token, and then present that token to
  Apigee Edge to be verified. (Same works with Google Sign-In. Or Paypal. Or
  Salesforce.com. etc)

* Asynchrony is required. For example, you want the client to send in a request,
  and then store that request somewhere, to be acted on by a separate system
  "later". That separate system will not have a synchronous connection to the
  client, and it may not have a direct connection to a central token dispensary.
  A JWT can be read by the asynchronous processing system to determine whether
  the work item can and should be fulfilled at that later time. This is, in a
  way, related to the Federation idea above. Be careful here, though: JWT
  expire. If the queue holding the work item does not get processed within the
  lifetime of the JWT, then the claims should no longer be trusted.

## Use opaque tokens when...

* There is no federation. The issuer of the token is the same party that
  validates the token. All API requests bearing the token will go through the
  token dispensary.

* There is no need or desire to allow the holder of the token to examine the
  claims within the token. When you wish to unilaterally allow token revocation.
  It is not possible to revoke JWT. They expire when they are marked to expire
  at creation time.

## Things that DON'T recommend one versus the other:

* custom claims. Both JWT and opaque OAuth tokens can carry custom claims about the subject.

* security. Both are bearer tokens. Both need to be protected as secrets.

* expiration. Both can be marked with an expiration. Both can be refreshed.

* The authentication mechanism or experience. Both can present the same user experience.

## When to use OAUTH2?

* service allows different clients/applications that act on behalf of
  someone/something (like FB apps, Google integration...)

* client must get access to resources of server

* content provider verifies user identity & requests permission to access its
  resources

"doing stuff on behalf of the user"

https://developer.okta.com/blog/2017/06/21/what-the-heck-is-oauth

-> centrale authorization endpoint?

> it decouples authentication from authorization and supports multiple use
  cases addressing different device capabilities.

> Client registration is also a key component of OAuth. It’s like the DMV of
  OAuth. You need to get a license plate for your application. This is how your
  app’s logo shows up in an authorization dialog.

-> we don't really want this?

## Conclusion

-> we're in a federation type system!

-> we don't want to maintain an authorization server, much less tap into the
   organization auth schemes (AD, other setups...)

-> OAUTH: You push state management onto each client developer.

# JWT Signing

https://tools.ietf.org/html/rfc7519

https://auth0.com/blog/json-web-token-signing-algorithms-overview/

* signing vs. encrypting -> signing: no tampering
* sign first, then use that as encrypted

## HMAC signing

* most common
* shared key

> HMACs are used with JWTs when you want a simple way for all parties to
  create and validate JWTs. Any party knowing the key can create new JWTs. In
  other words, with shared keys, it is possible for party to impersonate
  another one: HMAC JWTs do not provide guarantees with regards to the creator
  of the JWT. Anyone knowing the key can create one. For certain use cases,
  this is too permissive. This is where asymmetric algorithms come into play.

## RSA and ECDSA algorithms

> What asymmetric algorithms bring to the table is the possibility of verifying
  or decrypting a message without being able to create a new one.

## Shared key vs. RSA/ECDSA

* shared key a problem? key per organisatie -> api moet weten van welke
  organisatie JWT komt & dan juiste key selecteren -> beheer is vervelend

* API kan zelf keys maken, maar is geen probleem (NLX logt wat over lijn gaat)

* Developer bij request-org die key steelt kan impersonaten -> is ook probleem
  met private/public key encryption

* Assym encryption: org. signs met private key. Ontvanger moet testen tegen
  public key (public key moet ook vooraf gedeeld worden, net zoals shared secret!).

* kiezen voor gemak? er gaat geen gevoelige data in JWT over lijn...
