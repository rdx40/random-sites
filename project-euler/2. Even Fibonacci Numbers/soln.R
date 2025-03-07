even_fibonacci_sum <- function(limit) {
  a <- 1
  b <- 2
  total <- 0
  while (b <= limit) {
    if (b %% 2 == 0) {
      total <- total + b
    }
    temp <- a + b
    a <- b
    b <- temp
  }
  
  return(total)
}
print(even_fibonacci_sum(4000000))

