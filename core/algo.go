package core

// DispatchInFloors take a list of Team and compute all dispatch possibilities

// func combinaisonsRecChan(floor Floor, teams []Team, results chan<- Floor) {
// 	// fmt.Println("--->", floor)
// 	for k := range teams {
// 		// answer := Floor{append(floor.teams, teams[k])}
// 		results <- answer
// 		if len(teams[k+1:]) > 0 {
// 			combinaisonsRecChan(answer, teams[k+1:], results)
// 		}

// 	}
// }

// func computeAsync(alist []Team) {
// 	results := make(chan Floor)

// 	for k, el := range alist {
// 		go func(el Team) {
// 			results <- Floor{[]Team{el}}
// 		}(el)
// 		wg.Add(1)
// 		go func(el Team, k int) {
// 			defer wg.Done()
// 			combinaisonsRecChan(Floor{[]Team{el}}, alist[k+1:], results)
// 		}(el, k)
// 	}

// 	go func() {
// 		wg.Wait()
// 		close(results)
// 	}()
// 	nb := 0
// 	for range results {
// 		nb++
// 	}
// 	fmt.Println(nb)
// }
