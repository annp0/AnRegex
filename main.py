from regex import regex

if __name__ == "__main__":
    assert regex("(b|ab)*").match("babbab") == True
    assert regex(".*").match("random") == True
    r1 = regex("th(e|ere|ey|ose)")
    assert r1.match("the") == True
    assert r1.match("those") == True
    assert r1.match("ose") == False
    r2 = regex("(.*)at(.*)dot(com|edu)")
    assert r2.match("jewswoskiatmcmasterdotcom") == True
    assert r2.match("jewswoskiatmcmasterdotca") == False
    print("all tests passed")