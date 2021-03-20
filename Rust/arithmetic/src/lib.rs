//! Arithmetic Problem Solutions.
//!
//! Provides the solutions to problems 31 to 41 of the [`P99`]: Ninety-Nine Prolog Problems.
//!
//! [`P99`]: https://www.ic.unicamp.br/~meidanis/courses/mc336/2009s2/prolog/problemas/

use rand::Rng;
use std::convert::TryInto;
use std::f64;
use std::time::Instant;
use std::vec::Vec;

/// Determine whether a given integer is prime (P31).
pub fn is_prime(number: u64) -> bool {
    let upper_divisor = (number as f64).sqrt() as u64 + 1;
    for divisor in 2..upper_divisor {
        if number % divisor == 0 {
            return false;
        }
    }
    return true;
}

/// Determine the greatest common divisor of two positive integer numbers (P32).
pub fn gcd(a: u64, b: u64) -> u64 {
    // Euclid's Algorithm.
    if b == 0 {
        return a;
    } else {
        return gcd(b, a % b);
    }
}

/// Determine whether two positive integer numbers are coprime (P33).
pub fn are_coprime(a: u64, b: u64) -> bool {
    return gcd(a, b) == 1;
}

/// Calculate Euler's totient function phi(m) (P34).
pub fn totient_phi(m: u64) -> u64 {
    if m == 1 {
        return 1;
    }
    if is_prime(m) {
        return m - 1;
    }
    let mut co_primes = 1;
    for i in 2..(m / 2 + 1) {
        if m % i != 0 {
            if are_coprime(i, m) {
                co_primes += 1;
            }
        }
    }
    for i in (m / 2 + 1)..m {
        if are_coprime(i, m) {
            co_primes += 1;
        }
    }
    return co_primes;
}

/// Determine the prime factors of a given positive number (P35).
pub fn prime_factors(mut number: u64) -> Vec<u64> {
    let mut prime_factor_vec: Vec<u64> = Vec::new();
    if is_prime(number) {
        prime_factor_vec.push(number);
        return prime_factor_vec;
    }
    while number % 2 == 0 {
        prime_factor_vec.push(2);
        number = (number / 2) as u64;
    }
    for i in (3..((number as f64).sqrt() as u64 + 1)).step_by(2) {
        while number % i == 0 {
            prime_factor_vec.push(i);
            number = (number / i) as u64;
        }
    }
    if number > 2 {
        prime_factor_vec.push(number);
    }
    return prime_factor_vec;
}

/// Returns the length-encoded prime factor list of a positive integer number (P36).
pub fn prime_factors_encoded(number: u64) -> Vec<Vec<u64>> {
    let prime_factor_vec = prime_factors(number);
    let mut encoded: Vec<Vec<u64>> = Vec::new();
    let mut current = prime_factor_vec[0];
    let mut count = 1;
    for factor in prime_factor_vec[1..].iter() {
        if current != *factor {
            encoded.push(vec![count, current]);
            current = *factor;
            count = 1;
            continue;
        }
        count += 1;
    }
    encoded.push(vec![count, current]);
    return encoded;
}

/// Calculate Euler's totient function effectively (P37).
pub fn totient_phi_2(mut m: u64) -> u64 {
    if m == 1 {
        return 1;
    }
    let mut phi = 1;
    let prime_factors_encoded_vec = prime_factors_encoded(m);
    for elem in prime_factors_encoded_vec.iter() {
        m = elem[0];
        let p = elem[1];
        phi *= (p - 1) * p.pow((m - 1).try_into().unwrap());
    }
    return phi;
}

/// Compare the two methods of calculating Euler's totient function (P38).
pub fn compare_totient(tests: u64) {
    // Initiate random
    let mut rng = rand::thread_rng();
    println!("----------------------------------------------------------");
    println!("Argument\ttotient_phi (ns)\ttotient_phi_2 (ns)");
    println!("==========================================================");
    for _ in 0..tests {
        // Random number
        let m = rng.gen_range(1..20000);
        // Run totient phi
        let start_totient_phi = Instant::now();
        totient_phi(m);
        let elapsed_totient_phi = start_totient_phi.elapsed().as_nanos();
        // Run totient phi 2
        let start_totient_phi_2 = Instant::now();
        totient_phi_2(m);
        let elapsed_totient_phi_2 = start_totient_phi_2.elapsed().as_nanos();
        // Print Time
        println!(
            "{}\t\t{}\t\t\t{}",
            m, elapsed_totient_phi, elapsed_totient_phi_2
        );
    }
    println!("----------------------------------------------------------");
}

/// Return a list of prime numbers (P39).
pub fn prime_list(lower: u64, upper: u64) -> Vec<u64> {
    // Sieve of Eratosthenes
    let mut vec = vec![0; (upper + 1) as usize];
    for i in 2..((upper as f64).sqrt() as usize + 1) {
        if vec[i] == 0 {
            let mut j = i.pow(2);
            while j <= (upper as usize) {
                vec[j] = 1;
                j += i;
            }
        }
    }
    let mut prime_vec = Vec::new();
    for i in ((lower - 1) as usize)..((upper + 1) as usize) {
        if vec[i] == 0 {
            prime_vec.push(i as u64);
        }
    }
    return prime_vec;
}

/// Compute Goldbach's Conjecture.
pub fn goldbach(number: u64) -> Vec<u64> {
    if number <= 2 {
        panic!("The given number is smaller than 2.");
    }
    if number % 2 == 1 {
        panic!("The given number is odd.");
    }
    let mut prime = 0;
    for i in prime_list(3, number).iter() {
        if is_prime(number - i) {
            prime = *i;
            break;
        }
    }
    return vec![prime, number - prime];
}

/// Compute a list of Goldbach compositions.
pub fn goldbach_list(mut lower: u64, upper: u64) -> Vec<Vec<u64>> {
    let mut goldbach_vec: Vec<Vec<u64>> = Vec::new();
    if lower % 2 == 1 {
        lower += 1;
    }
    for i in ((lower as usize)..(upper as usize + 1)).step_by(2) {
        goldbach_vec.push(goldbach(i as u64));
    }
    return goldbach_vec;
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_prime() {
        assert_eq!(is_prime(7), true);
        assert_eq!(is_prime(31), true);
        assert_eq!(is_prime(101), true);
        assert_eq!(is_prime(49), false);
        assert_eq!(is_prime(122), false);
    }

    #[test]
    fn test_gcd() {
        assert_eq!(gcd(36, 63), 9);
        assert_eq!(gcd(78, 32), 2);
        assert_eq!(gcd(35, 49), 7);
        assert_eq!(gcd(32, 112), 16);
        assert_eq!(gcd(33, 132), 33);
    }

    #[test]
    fn test_are_coprime() {
        assert_eq!(are_coprime(35, 64), true);
        assert_eq!(are_coprime(35, 49), false);
        assert_eq!(are_coprime(35, 56), false);
    }

    #[test]
    fn test_totient_phi() {
        assert_eq!(totient_phi(10), 4);
        assert_eq!(totient_phi(17), 16);
        assert_eq!(totient_phi(39), 24);
        assert_eq!(totient_phi(198), 60);
        assert_eq!(totient_phi(24420), 5760);
    }

    #[test]
    fn test_prime_factors() {
        assert_eq!(prime_factors(315), vec![3, 3, 5, 7]);
        assert_eq!(prime_factors(430), vec![2, 5, 43]);
        assert_eq!(prime_factors(728), vec![2, 2, 2, 7, 13]);
        assert_eq!(prime_factors(999), vec![3, 3, 3, 37]);
        assert_eq!(prime_factors(1725), vec![3, 5, 5, 23]);
    }

    #[test]
    fn test_prime_factors_encoded() {
        assert_eq!(
            prime_factors_encoded(315),
            vec![vec![2, 3], vec![1, 5], vec![1, 7]]
        );
        assert_eq!(
            prime_factors_encoded(430),
            vec![vec![1, 2], vec![1, 5], vec![1, 43]]
        );
        assert_eq!(
            prime_factors_encoded(728),
            vec![vec![3, 2], vec![1, 7], vec![1, 13]]
        );
        assert_eq!(prime_factors_encoded(999), vec![vec![3, 3], vec![1, 37]]);
        assert_eq!(
            prime_factors_encoded(1725),
            vec![vec![1, 3], vec![2, 5], vec![1, 23]]
        );
    }

    #[test]
    fn test_totient_phi_2() {
        assert_eq!(totient_phi_2(10), 4);
        assert_eq!(totient_phi_2(17), 16);
        assert_eq!(totient_phi_2(39), 24);
        assert_eq!(totient_phi_2(198), 60);
        assert_eq!(totient_phi_2(24420), 5760);
    }

    #[test]
    fn test_compare_totient() {
        compare_totient(10);
        compare_totient(50);
    }

    #[test]
    fn test_prime_list() {
        assert_eq!(prime_list(9, 41), vec![11, 13, 17, 19, 23, 29, 31, 37, 41]);
        assert_eq!(
            prime_list(3923, 4002),
            vec![3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001]
        );
        assert_eq!(prime_list(5003, 5024), vec![5003, 5009, 5011, 5021, 5023]);
        assert_eq!(prime_list(283, 312), vec![283, 293, 307, 311]);
        assert_eq!(prime_list(2131, 2142), vec![2131, 2137, 2141]);
    }

    #[test]
    fn test_goldbach() {
        assert_eq!(goldbach(28), vec![5, 23]);
        assert_eq!(goldbach(30), vec![7, 23]);
        assert_eq!(goldbach(1002), vec![5, 997]);
        assert_eq!(goldbach(1004), vec![7, 997]);
        assert_eq!(goldbach(10000), vec![59, 9941]);
        assert_eq!(goldbach(5000), vec![7, 4993]);
    }

    #[test]
    fn test_goldbach_list() {
        assert_eq!(
            goldbach_list(9, 20),
            vec![
                vec![3, 7],
                vec![5, 7],
                vec![3, 11],
                vec![3, 13],
                vec![5, 13],
                vec![3, 17]
            ]
        );
        assert_eq!(
            goldbach_list(28, 36),
            vec![
                vec![5, 23],
                vec![7, 23],
                vec![3, 29],
                vec![3, 31],
                vec![5, 31]
            ]
        );
        assert_eq!(
            goldbach_list(240, 246),
            vec![vec![7, 233], vec![3, 239], vec![3, 241], vec![5, 241]]
        );
    }
}
