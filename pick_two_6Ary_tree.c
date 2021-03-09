/*
 * The following coding problem : There is bag that contains 3 colours of ball (Red, Green & Blue). Numbers of ball count of each colours are A, B, and C respectively. We will have 3 picks and in each pick we will take 2 balls out and we won’t replace the picked balls for subsequent picks or draws. We wanted to find out the probability of picking balls of same colour in 3rd draw. You are NOT allowed to use “conditional probability” formulae to solve this, instead solve algorithmically using data structure.
 *
 */

#include<stdio.h>
#include<stdlib.h>

// defining structure for six ary tree node
// each node will store the number of balls remaining of each type, the draw number in which the current node is present, the ...
// ... colors chosen to arrive at the current node, the probability of arriving at current node and the pointers to all six nodes that...
// ... can be reached from current node by choosing one of the six possibilities -- 0 : {A,A}; 1 : {B, B}; 2 : {C,C}; 3 : {A,B}, 4 : {A,C}, 5 : {B,C} 
typedef struct six_ary_tree_node{
	int num_ball_A, num_ball_B, num_ball_C;
	int draw_number;
	int colors_chosen; // 0 : {A,A}; 1 : {B, B}; 2 : {C,C}; 3 : {A,B}, 4 : {A,C}, 5 : {B,C}, -1 : NULL
	double current_node_probability;
	struct six_ary_tree_node* Children_Nodes;
}node;

// computing n choose 2
int n_choose_2(int n){
	return (n*(n-1))/2;
}

// creating the probability tree ...
// ... The input arguments : 
// ---the pointer to current node
// ---number of balls remaining of each type
// ---the number of draws after which the current node was reached
// ---the probabiity of arriving at the current node
// ---the colors that were chosen to arrive at the current node
void create_tree(node* root, int num_ball_A, int num_ball_B, int num_ball_C, int draw_number, double current_node_probability, 
		int colors_chosen){
	root->num_ball_A = num_ball_A;
	root->num_ball_B = num_ball_B;
	root->num_ball_C = num_ball_C;
	root->draw_number = draw_number;
	root->current_node_probability = current_node_probability;
	root->colors_chosen = colors_chosen;
	/* Checking draw_number of current node as we are having three draws */
	if(draw_number!=3){
		root->Children_Nodes = (node*) malloc(sizeof(node)*6);
		int total_num_balls = num_ball_A + num_ball_B  + num_ball_C;
		/*picking 2 'A' balls in the next draw*/
		if(num_ball_A >= 2){
		    create_tree(&(root->Children_Nodes[0]), num_ball_A - 2, num_ball_B, num_ball_C,
		         	    draw_number + 1, 
				    current_node_probability * ((double)n_choose_2(num_ball_A)/n_choose_2(total_num_balls)),
				0);
		}
		else{
		    root->Children_Nodes[5].draw_number = -1;
		}

		/*picking 2 'B' balls in the next draw*/
		if(num_ball_B >= 2){
		    create_tree(&(root->Children_Nodes[1]), num_ball_A, num_ball_B - 2, num_ball_C,
		    		    draw_number + 1, 
		    		    current_node_probability * ((double)n_choose_2(num_ball_B)/n_choose_2(total_num_balls)),
				1);
	        }
		else{
		    root->Children_Nodes[5].draw_number = -1;
		}

		/*picking 2 'C' balls in the next draw*/
		if(num_ball_C >= 2){
		    create_tree(&(root->Children_Nodes[2]), num_ball_A, num_ball_B, num_ball_C - 2,
				    draw_number + 1, 
				    current_node_probability * ((double)n_choose_2(num_ball_C)/n_choose_2(total_num_balls)),
				2);
		}
		else{
		    root->Children_Nodes[5].draw_number = -1;
		}

		/*picking 1 'A' ball and 1 'B' ball in the next draw*/
		if((num_ball_A >= 1) && (num_ball_B >= 1)){
		    create_tree(&(root->Children_Nodes[3]), num_ball_A - 1, num_ball_B - 1, num_ball_C,
		  		    draw_number + 1, 
				    current_node_probability * ((double)(num_ball_A * num_ball_B)/n_choose_2(total_num_balls)),
				3);
		}
		else{
		    root->Children_Nodes[5].draw_number = -1;
		}

		/*picking 1 'A' ball and 1 'C' ball in the next draw*/
		if((num_ball_A >= 1) && (num_ball_C >= 1)){
		    create_tree(&(root->Children_Nodes[4]), num_ball_A - 1, num_ball_B, num_ball_C - 1,
				    draw_number + 1, 
				    current_node_probability * ((double)(num_ball_A * num_ball_C)/n_choose_2(total_num_balls)),
				4);
		}
		else{
		    root->Children_Nodes[5].draw_number = -1;
		}

		/*picking 1 'B' ball and 1 'C' ball in the next draw*/
		if((num_ball_B >= 1) && (num_ball_C >= 1)){
		    create_tree(&(root->Children_Nodes[5]), num_ball_A, num_ball_B - 1, num_ball_C - 1,
				    draw_number + 1, 
				    current_node_probability * ((double)(num_ball_B * num_ball_C)/n_choose_2(total_num_balls)),
				5);
		}
		else{
		    root->Children_Nodes[5].draw_number = -1;
		}
	}
	else{
	    root->Children_Nodes = NULL;
	}
}

// printing all the nodes in current tree --- depth first
void print_tree(node root_node){

    printf("----------------------------------------------------\n");
    printf("Draw number of the current node : %d\n",root_node.draw_number);
    if(root_node.colors_chosen == 0){printf("Colors chosen in the current node : {A,A}\n");}
    if(root_node.colors_chosen == 1){printf("Colors chosen in the current node : {B,B}\n");}
    if(root_node.colors_chosen == 2){printf("Colors chosen in the current node : {C,C}\n");}
    if(root_node.colors_chosen == 3){printf("Colors chosen in the current node : {A,B}\n");}
    if(root_node.colors_chosen == 4){printf("Colors chosen in the current node : {A,C}\n");}
    if(root_node.colors_chosen == 5){printf("Colors chosen in the current node : {B,C}\n");}
    if(root_node.colors_chosen == -1){printf("Colors chosen in the current node : NULL\n");}
    printf("Probability of the current node : %lf\n",root_node.current_node_probability);
    printf("Number of 'A' balls remaining in the current node : %d\n",root_node.num_ball_A);
    printf("Number of 'B' balls remaining in the current node : %d\n",root_node.num_ball_B);
    printf("Number of 'C' balls remaining in the current node : %d\n",root_node.num_ball_C);
    printf("\n");

    if(root_node.Children_Nodes != NULL){
        for(int i=0; i<6; i++){
	        if(root_node.Children_Nodes[i].draw_number!=-1){print_tree(root_node.Children_Nodes[i]);}
        }
    }
}

// finding the probability that the colors chosen in draw number 3 are of same color 
void find_result(node root_node, double* result_ptr){
	if(root_node.draw_number == 3 && (root_node.colors_chosen==0 || root_node.colors_chosen==1 || root_node.colors_chosen==2)){
		*result_ptr = (*result_ptr) + root_node.current_node_probability;
	}

    if(root_node.Children_Nodes != NULL){
        for(int i=0; i<6; i++){
	        if(root_node.Children_Nodes[i].draw_number!=-1){find_result(root_node.Children_Nodes[i],result_ptr);}
        }
    }
}

// Taking number of balls of color A,B,C as input (and then creating tree, printing tree and computing result)
int main(){
    int A, B, C;
    printf("Please input number of balls of first colour -- A : ");
    scanf("%d",&A);
    printf("Please input number of balls of second colour -- B : ");
    scanf("%d",&B);
    printf("Please input number of balls of third colour -- C : ");
    scanf("%d",&C);

    node root_node;
    create_tree(&(root_node), A, B, C, 0, 1, -1);

    print_tree(root_node);

    double result;
    find_result(root_node, &result);

    printf("--------------------------");
    printf("\n\nResult : %lf\n\n", result);
    printf("--------------------------");
    printf("\n");

    return 0;
}
