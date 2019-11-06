from Profile import Profile

ami = Profile()
ami.setName("Amos", "Asherov")
ami.setGender("Male")
ami.setBirthday("24/06/1995")
address = {
            "Country": "Israel",
            "City": "Bat Yam",
            "Address": "Nissenbaum 37",
            "Zip": "75575"}
ami.setAddress(address)
ami.setHome(7, 10)
ami.setCurrent(5, 8)
ami.toString()
