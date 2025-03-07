sum_multiples <- function(limit){
	numbers <- 1:(limit-1)
	multiples <- numbers[numbers %% 3 ==0 | numbers %% 5 == 0]
	sum(multiples)
}
cat(sum_multiples(1000))

