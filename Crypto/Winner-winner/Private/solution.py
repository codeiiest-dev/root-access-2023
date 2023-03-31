n = 147695825873258199075309315014079443936086332837178250613274696838114905688236190451470147800918349214195035282891570360210898000592369649486597168614329853219598993273421509047977797008168968025564056199032515406736798948561048292476945071024301402247869004043825355544373600364624400951703065712509703991387235358817700171631149589377493407337127440336067207739807995868819073922238789109634380541865675900696065061443898050487798987046425304452427508409865302367453064543439584974205069130145255332389986798217364903361079863215463518779949872986076073243793794093151729378782051087439601217312467
e = 138717416281337456692344455554891152247979574963839091521068849245832916684241545687054126952507149696814492808454926496019498942776996020057244451765709930826435581912376373047603435911804572092248095687948006408704452452256665944166346933887797474711181206505224728485212472995938850988624267301780146970431846042161484072392886829360818890732741950878725428152877001088273188939463216251763263843902956942160456673351898835449942075351850191418546600584698773068083458447115589186227617300982080578801411743675190283374770927582403134122446145359617714684008991806559599732081315258849269495501827
ct = 28687321513512720229641020267062143933513049102750816891659892149280866327732202523267134530465205269598978157637398029355743402151270896658968465159616111025494757501743377076328250133926005444027755945805698078947476552993585452925428432544547215158377737915959018942303777087794933239163055875489936403178270829853103307466424490515113597381990437211289379794880760878804904618538863135147617798449764861900246759044612639917391048960840770641139180883550797042444366092240121351517070092705174245047452905172992379998647473236449538678498363170182642665915051840825042946518301279422637159205395

from Crypto.Util.number import long_to_bytes

def rational_to_contfrac(x,y):
    '''
    Converts a rational x/y fraction into
    a list of partial quotients [a0, ..., an]
    '''
    a = x//y
    pquotients = [a]
    while a * y != x:
        x,y = y,x-a*y
        a = x//y
        pquotients.append(a)
    return pquotients


def convergents_from_contfrac(frac):
    '''
    computes the list of convergents
    using the list of partial quotients
    '''
    convs = [];
    for i in range(len(frac)):
        convs.append(contfrac_to_rational(frac[0:i]))
    return convs


def contfrac_to_rational (frac):
    '''Converts a finite continued fraction [a0, ..., an]
     to an x/y rational.
     '''
    if len(frac) == 0:
        return (0,1)
    num = frac[-1]
    denom = 1
    for _ in range(-2,-len(frac)-1,-1):
        num, denom = frac[_]*num+denom, num
    return (num,denom)


def isqrt(n):
    '''
    Calculates the integer square root
    for arbitrary large nonnegative integers
    '''
    if n < 0:
        raise ValueError('square root not defined for negative numbers')

    if n == 0:
        return 0
    a, b = divmod(len(bin(n)) - 2, 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def is_perfect_square(n):
    '''
    If n is a perfect square it returns sqrt(n),

    otherwise returns -1
    '''
    h = n & 0xF; #last hexadecimal "digit"

    if h > 9:
        return -1 # return immediately in 6 cases out of 16.

    # Take advantage of Boolean short-circuit evaluation
    if ( h != 2 and h != 3 and h != 5 and h != 6 and h != 7 and h != 8 ):
        # take square root if you must
        t = isqrt(n)
        if t*t == n:
            return t
        else:
            return -1

    return -1


def hack_RSA(e,n):
    '''
    Finds d knowing (e,n)
    applying the Wiener continued fraction attack
    '''
    frac = rational_to_contfrac(e, n)
    convergents = convergents_from_contfrac(frac)

    for (k,d) in convergents:

        #check if d is actually the key
        if k!=0 and (e*d-1)%k == 0:
            phi = (e*d-1)//k
            s = n - phi + 1
            # check if the equation x^2 - s*x + n = 0
            # has integer roots
            discr = s*s - 4*n
            if(discr>=0):
                t = is_perfect_square(discr)
                if t!=-1 and (s+t)%2==0:
                    print("Hacked!")
                    return d

d = hack_RSA(e, n)
print(long_to_bytes(pow(ct, d, n)))