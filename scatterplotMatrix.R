library(ggplot2)
library(GGally)

# Bring dataset into memory
attach(iris)

# Verify the structure of the data
head(iris, 10)
str(iris)

# Make any necessary datatype changes
iris$Sepal.Length <- as.numeric(iris$Sepal.Length)

# Isolate only those columns which are numeric/continuous
num_only <- unlist(lapply(iris, is.numeric))

# Create regression line function
panel.lm <- function(x, y, pch=par("pch"), col.lm="red", ...){
  ymin <- min(y)
  ymax <- max(y)
  xmin <- min(x)
  xmax <- max(x)
  ylim <- c(min(ymin,xmin),max(ymax,xmax))
  xlim <- ylim
  points(x, y, pch = pch,ylim = ylim, xlim= xlim,...)
  ok <- is.finite(x) & is.finite(y)
  if (any(ok)) 
    abline(lm(y[ok]~ x[ok]), 
           col = col.lm, ...)
}

# Output Scatterplot Version 1
pairs(iris[,num_only], panel = panel.lm)

# Output Scatterplot Version 2
ggpairs(iris[,num_only], ggplot2::aes(colour=iris$Species),  panel = panel.lm)
      