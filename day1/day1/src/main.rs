
use std::fs;

fn main(){
    let content = fs::read_to_string("day1_input.txt").expect("Reading day1_input.txt");

    let lines = content.split("\n").collect::<Vec<&str>>();

    let mut partial_sums = <Vec<u32>>::new();

    let mut temp_sum:u32 = 0;
    for line in lines.iter(){
        let abc:&str  = line.trim();
        match abc {
            "" => {
                partial_sums.push(temp_sum);
                temp_sum = 0;
            }
            _ => {
                let val:u32 = abc.parse::<u32>().unwrap();
                temp_sum += val;
            }

        }
    }

    partial_sums.sort();

    let the_most:&u32 = partial_sums.last().unwrap();

    let the_sum:u32 = partial_sums.iter().rev().take(3).sum();

    println!("The Most: {}", the_most);
    println!("Top 3 Sum: {}", the_sum);

}