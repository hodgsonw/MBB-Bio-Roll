library(remotes)
supported_bioc = "3.3"

#expected inputs, list of packages with URLS, and potentially versions

#check for proxy server

#If none available Download Directly using Devtools, or remotes
download <- function(name, version = NULL, location = "cran") {
#can come from cran, bioconductor, github
#might have to provide argument that specifies method of download (libcurl, etc)
  if (location == "cran") {
 
#needs to pass build arguments potentially 
    remotes::install_version(name, version, build = FALSE, Ncpus = 24, repos = "http://cran.utstat.utoronto.ca")
  }
  
  if (location == "bioconductor") {
  
    bioc_package = name
  
#not working not valid bioc repo
    if (supported_bioc != "") bioc_package = paste(supported_bioc, "/", name)
    remotes::install_bioc(bioc_package, build = FALSE)
  }
  
  if (location == "github") {
  
#not working couldnt find package in repo
    github_repo = name 
    remotes::install_github(github_repo, build = FALSE)
  }


}

#cache downloaded packages if proxy is available and
#report status of download
