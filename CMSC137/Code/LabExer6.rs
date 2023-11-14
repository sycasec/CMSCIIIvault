use std::io;

fn main() {
    let mut input = String::new();
    io::stdin()
        .read_line(&mut input)
        .expect("Failed to read from stdin");

    let clean_input = input.trim().to_lowercase();

    match clean_input.as_str() {
        "1" => simple_parity_check(),
        "2" => twod_parity_check(),
        "3" => checksum(),
        "4" => crc(),
        _ => {
            println!("Invalid input. Please enter valid integer (1-4)");
        }
    }
}

// ----------------  helper functions -------------------------

fn validate_bits(input: &str) -> i32 {
    let mut ones_count = 0;

    for c in input.chars() {
        match c {
            '0' => continue,
            '1' => ones_count += 1,
            _ => panic!("Illegal character: '{}'", c),
        }
    }
    ones_count
}

// fn calculate_errors(matrix: &Vec<Vec<char>>) -> i32 {};

// ----------------  user functions -------------------------

fn simple_parity_check() {
    let mut dataword = String::new();
    let mut codeword = String::new();

    io::stdin()
        .read_line(&mut dataword)
        .expect("Failed to read dataword");

    io::stdin()
        .read_line(&mut codeword)
        .expect("Failed to read codeword");

    let dword_count = validate_bits(dataword.trim());
    let cword_count = validate_bits(codeword.trim());
    dataword = dataword.trim().to_string();
    codeword = codeword.trim().to_string();

    if dword_count % 2 == 0 {
        dataword.push_str("0");
        println!("Codeword: {}", dataword);
    } else if dword_count % 2 != 0 {
        dataword.push_str("1");
        println!("Codeword: {}", dataword);
    }

    if cword_count % 2 == 0 {
        codeword.pop().unwrap();
        println!("Data word: {}", codeword);
    } else {
        println!("Data word: Discarded");
    }
}

fn twod_parity_check() {
    let mut input_string = String::new();
    io::stdin()
        .read_line(&mut input_string)
        .expect("Failed to read input string");
    input_string = input_string.trim().to_string();

    if input_string.len() < 45 {
        panic!(
            "Input string must have 45 characters: len={}",
            input_string.len()
        );
    }

    let temp_vec: Vec<char> = input_string.chars().collect();
    let mut matrix: Vec<Vec<char>> = vec![vec![' '; 9]; 5];
    let mut col_count: Vec<i32> = vec![0; 8];
    let mut row_count: Vec<i32> = vec![0; 4];

    let mut row = 0;
    let mut col = 0;
    // let mut cc = 0;
    let mut rc = 0;
    for ch in temp_vec.iter() {
        matrix[row][col] = *ch;
        if *ch == '1' && col < 8 && row < 4 {
            rc += 1;
            col_count[col] += 1;
        }
        col += 1;
        if col == 9 {
            col = 0;
            if row < 4 {
                row_count[row] = rc;
            }
            rc = 0;
            row += 1;
        }
        if row == 5 {
            break;
        }
    }
    println!("row_count = {:?}\ncol_count = {:?}", row_count, col_count);

    for row in &matrix {
        for char in row {
            print!("{} ", char);
        }
        println!();
    }

    let mut error_count = 0;

    for i in 0..8 {
        if (matrix[4][i] == '1' && col_count[i] % 2 == 0)
            || (matrix[4][i] == '0' && col_count[i] % 2 != 0)
        {
            error_count += 1;
        }
    }
    for i in 0..4 {
        if (matrix[i][8] == '1' && row_count[i] % 2 == 0)
            || (matrix[i][8] == '0' && row_count[i] % 2 != 0)
        {
            error_count += 1;
        }
    }
    let mut final_rc = 0;
    let mut final_cc = 0;
    for i in 0..8 {
        if matrix[4][i] == '1' {
            final_rc += 1;
        }
    }
    for i in 0..4 {
        if matrix[i][8] == '1' {
            final_cc += 1;
        }
    }

    if (final_rc % 2 == 0 && matrix[4][8] == '1') || (final_rc % 2 != 0 && matrix[4][8] == '0') {
        error_count += 1;
    }
    if (final_cc % 2 == 0 && matrix[4][8] == '1') || (final_cc % 2 != 0 && matrix[4][8] == '0') {
        error_count += 1;
    }
    println!("Error count: {}", error_count);
}

fn checksum() {
    let mut rcv_msg = String::new();
    io::stdin()
        .read_line(&mut rcv_msg)
        .expect("Failed to read input string");

    let k = 8;
    let c1 = &rcv_msg[0..k];
    let c2 = &rcv_msg[k..2 * k];
    let c3 = &rcv_msg[2 * k..3 * k];
    let c4 = &rcv_msg[3 * k..4 * k];
    let checksum = &rcv_msg[4 * k..5 * k];

    println!("cheksum = {}", checksum);
}

fn crc() {
    println!("crc");
}
