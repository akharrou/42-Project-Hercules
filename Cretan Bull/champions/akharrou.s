.name "akharrou"
.comment "You already lost."

l2:		sti r1, %:live, %1
		and r1, %0, r1

live:	live %1
		live %-42
		zjmp %:live
