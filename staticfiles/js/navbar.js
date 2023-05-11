
const friendsIcon = document.getElementById("friends")
const plansIcon = document.getElementById("plans")
const exploreIcon = document.getElementById("explore")
const searchIcon = document.getElementById("search")
const friendsExtended = document.getElementById("friends_extended")
const plansExtended = document.getElementById("plans_extended")
const exploreExtended = document.getElementById("explore_extended")




friendsIcon.addEventListener("click", ToggleNavbar_Friend)
plansIcon.addEventListener("click", ToggleNavbar_Plans)
exploreIcon.addEventListener("click", ToggleNavbar_Explore)

function ToggleNavbar_Friend() {

    if (friendsExtended.className == "li_hidden")
        friendsExtended.className = "extended",
            plansExtended.className = "li_hidden",
            exploreExtended.className = "li_hidden";

    else
        friendsExtended.className = "li_hidden";
}

function ToggleNavbar_Plans() {

    if (plansExtended.className == "li_hidden")
        plansExtended.className = "extended";
    else
        plansExtended.className = "li_hidden"
    friendsExtended.className = "li_hidden"
    exploreExtended.className = "li_hidden";
}

function ToggleNavbar_Explore() {

    if (exploreExtended.className == "li_hidden")
        exploreExtended.className = "extended";
    else
        exploreExtended.className = "li_hidden"
    plansExtended.className = "li_hidden"
    friendsExtended.className = "li_hidden";
}








