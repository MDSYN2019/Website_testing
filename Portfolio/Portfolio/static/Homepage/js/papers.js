function AcademicPaper (name, year, paper) {
    this.name = name;
    this.year = year;
    this.paper = paper;
}

function makePerson(first, last) {
    this.first = first;
    this.last = last;
    this.fullName = function() {
	return this.first + ' ' + this.last;
    };

    this.fullNameReversed = function() {
	return this.last + ', ' + this.first;
    };
    
}


