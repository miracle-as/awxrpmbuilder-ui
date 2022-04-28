var packagestatus = document.getElementById("packagestatus").innerHTML
var packagesourcefilestatus = document.getElementById("packagesourcefilestatus").innerHTML
var packageorgspecfilestatus = document.getElementById("packageorgspecfilestatus").innerHTML
var packagespecfilestatus = document.getElementById("packagespecfilestatus").innerHTML
var packagerpmfilestatus = document.getElementById("packagerpmfilestatus").innerHTML
var packageSclfilestatus = document.getElementById("packageSclfilestatus").innerHTML
var packagesclrpmfilestatus = document.getElementById("packagesclrpmfilestatus").innerHTML

//
if (packagestatus == "Building") {
    document.getElementById("packagestatus").style.backgroundColor = "Light yellow4";
} else if (packagestatus == "Completed") {
    document.getElementById("packagestatus").style.backgroundColor = "limegreen";
} else if (packagestatus == "Failed") {
    document.getElementById("packagestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packagestatus").style.backgroundColor = "gainsboro";
}
//
if (packagesourcefilestatus == "Building") {
    document.getElementById("packagesourcefilestatus").style.backgroundColor = "Light yellow4";
} else if (packagesourcefilestatus == "Completed") {
    document.getElementById("packagesourcefilestatus").style.backgroundColor = "limegreen";
} else if (packagesourcefilestatus == "Failed") {
    document.getElementById("packagesourcefilestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packagesourcefilestatus").style.backgroundColor = "gainsboro";
}
//
if (packageorgspecfilestatus == "Building") {
    document.getElementById("packageorgspecfilestatus").style.backgroundColor = "Light yellow4";
} else if (packageorgspecfilestatus == "Completed") {
    document.getElementById("packageorgspecfilestatus").style.backgroundColor = "limegreen";
} else if (packageorgspecfilestatus == "Failed") {
    document.getElementById("packageorgspecfilestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packageorgspecfilestatus").style.backgroundColor = "gainsboro";
}
//
if (packagespecfilestatus == "Building") {
    document.getElementById("packagespecfilestatus").style.backgroundColor = "Light yellow4";
} else if (packagespecfilestatus == "Completed") {
    document.getElementById("packagespecfilestatus").style.backgroundColor = "limegreen";
} else if (packagespecfilestatus == "Failed") {
    document.getElementById("packagespecfilestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packagespecfilestatus").style.backgroundColor = "gainsboro";
}
//
if (packagerpmfilestatus == "Building") {
    document.getElementById("packagerpmfilestatus").style.backgroundColor = "Light yellow4";
} else if (packagerpmfilestatus == "Completed") {
    document.getElementById("packagerpmfilestatus").style.backgroundColor = "limegreen";
} else if (packagerpmfilestatus == "Failed") {
    document.getElementById("packagerpmfilestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packagerpmfilestatus").style.backgroundColor = "gainsboro";
}
//
if (packageSclfilestatus == "Building") {
    document.getElementById("packageSclfilestatus").style.backgroundColor = "Light yellow4";
} else if (packageSclfilestatus == "Completed") {
    document.getElementById("packageSclfilestatus").style.backgroundColor = "limegreen";
} else if (packageSclfilestatus == "Failed") {
    document.getElementById("packageSclfilestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packageSclfilestatus").style.backgroundColor = "gainsboro";
}
//
if (packagesclrpmfilestatus == "Building") {
    document.getElementById("packagesclrpmfilestatus").style.backgroundColor = "Light yellow4";
} else if (packagesclrpmfilestatus == "Completed") {
    document.getElementById("packagesclrpmfilestatus").style.backgroundColor = "limegreen";
} else if (packagesclrpmfilestatus == "Failed") {
    document.getElementById("packagesclrpmfilestatus").style.backgroundColor = "red";
} else {
    document.getElementById("packagesclrpmfilestatus").style.backgroundColor = "gainsboro";
}