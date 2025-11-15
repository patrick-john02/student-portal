<script lang="ts">
export const description = "Admin dashboard overview"
export const iframeHeight = "800px"
export const containerClass = "w-full h-full"
</script>

<script setup lang="ts">
import AppSidebar from "@/components/sidebars/AppSidebar.vue"
import {
  Breadcrumb,
  BreadcrumbItem,
  BreadcrumbLink,
  BreadcrumbList,
  BreadcrumbPage,
  BreadcrumbSeparator,
} from "@/components/ui/breadcrumb"
import { Separator } from "@/components/ui/separator"
import {
  SidebarInset,
  SidebarProvider,
  SidebarTrigger,
} from "@/components/ui/sidebar"
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { 
  Users, 
  GraduationCap, 
  BookOpen, 
  Calendar,
  TrendingUp,
  Bell,
  Clock,
  AlertCircle,
  CheckCircle,
  DollarSign,
  UserCheck,
  ArrowRight
} from "lucide-vue-next"

const userRole = 'Admin'

// Mock data
const recentActivities = [
  { id: 1, action: 'New student enrolled', user: 'John Doe', time: '2 minutes ago', type: 'enrollment' },
  { id: 2, action: 'Grade submitted', user: 'Ms. Smith', time: '15 minutes ago', type: 'grade' },
  { id: 3, action: 'Payment received', user: 'Jane Wilson', time: '1 hour ago', type: 'payment' },
  { id: 4, action: 'Assignment created', user: 'Mr. Johnson', time: '2 hours ago', type: 'assignment' },
  { id: 5, action: 'Attendance recorded', user: 'Ms. Davis', time: '3 hours ago', type: 'attendance' },
]

const upcomingEvents = [
  { id: 1, title: 'Midterm Examinations', date: 'Nov 20-24, 2025', type: 'exam' },
  { id: 2, title: 'Parent-Teacher Conference', date: 'Nov 28, 2025', type: 'meeting' },
  { id: 3, title: 'School Foundation Day', date: 'Dec 5, 2025', type: 'event' },
]

const pendingTasks = [
  { id: 1, task: 'Review 12 pending enrollments', priority: 'high' },
  { id: 2, task: 'Approve 5 teacher leave requests', priority: 'medium' },
  { id: 3, task: 'Update school calendar', priority: 'low' },
]
</script>

<template>
  <SidebarProvider>
    <AppSidebar :user-role="userRole" />
    <SidebarInset>
      <header class="flex h-16 shrink-0 items-center gap-2 transition-[width,height] ease-linear group-has-data-[collapsible=icon]/sidebar-wrapper:h-12">
        <div class="flex items-center gap-2 px-4">
          <SidebarTrigger class="-ml-1" />
          <Separator orientation="vertical" class="mr-2 h-4" />
          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem class="hidden md:block">
                <BreadcrumbLink href="/admin/dashboard">
                  Admin
                </BreadcrumbLink>
              </BreadcrumbItem>
              <BreadcrumbSeparator class="hidden md:block" />
              <BreadcrumbItem>
                <BreadcrumbPage>Dashboard</BreadcrumbPage>
              </BreadcrumbItem>
            </BreadcrumbList>
          </Breadcrumb>
        </div>
        <div class="ml-auto flex items-center gap-2 px-4">
          <Button variant="outline" size="sm">
            <Bell class="h-4 w-4" />
          </Button>
        </div>
      </header>

      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Welcome Section -->
        <div class="rounded-lg border bg-gradient-to-r from-primary/10 via-primary/5 to-background p-6">
          <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div>
              <h2 class="text-3xl font-bold">Welcome back, Admin!</h2>
              <p class="text-muted-foreground mt-2">Saturday, November 15, 2025 • Here's what's happening today.</p>
            </div>
            <div class="flex gap-2">
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                Schedule
              </Button>
              <Button>
                <TrendingUp class="mr-2 h-4 w-4" />
                View Analytics
              </Button>
            </div>
          </div>
        </div>

        <!-- Today's Quick Stats -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card className="border-l-4 border-l-blue-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Students Present</CardTitle>
              <UserCheck class="h-4 w-4 text-blue-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">1,210 / 1,284</div>
              <p class="text-xs text-muted-foreground mt-1">
                94.2% attendance today
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-l-green-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Active Classes</CardTitle>
              <BookOpen class="h-4 w-4 text-green-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">32</div>
              <p class="text-xs text-muted-foreground mt-1">
                Out of 42 total classes
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-l-orange-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">Pending Tasks</CardTitle>
              <AlertCircle class="h-4 w-4 text-orange-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">12</div>
              <p class="text-xs text-muted-foreground mt-1">
                3 high priority items
              </p>
            </CardContent>
          </Card>

          <Card className="border-l-4 border-l-purple-500">
            <CardHeader class="flex flex-row items-center justify-between space-y-0 pb-2">
              <CardTitle class="text-sm font-medium">New Notifications</CardTitle>
              <Bell class="h-4 w-4 text-purple-500" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">8</div>
              <p class="text-xs text-muted-foreground mt-1">
                Since last login
              </p>
            </CardContent>
          </Card>
        </div>

        <!-- Main Content Grid -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
          <!-- Recent Activities -->
          <Card class="col-span-4">
            <CardHeader class="flex flex-row items-center justify-between">
              <div>
                <CardTitle>Recent Activities</CardTitle>
                <CardDescription>Latest actions and updates across the system</CardDescription>
              </div>
              <Button variant="ghost" size="sm">View All</Button>
            </CardHeader>
            <CardContent>
              <div class="space-y-3">
                <div v-for="activity in recentActivities" :key="activity.id" class="flex items-center gap-4 p-3 rounded-lg border hover:bg-muted/50 transition-colors cursor-pointer">
                  <div :class="[
                    'flex h-10 w-10 items-center justify-center rounded-full',
                    activity.type === 'enrollment' ? 'bg-blue-100 dark:bg-blue-900' :
                    activity.type === 'grade' ? 'bg-green-100 dark:bg-green-900' :
                    activity.type === 'payment' ? 'bg-purple-100 dark:bg-purple-900' :
                    'bg-orange-100 dark:bg-orange-900'
                  ]">
                    <CheckCircle v-if="activity.type === 'enrollment'" class="h-5 w-5 text-blue-600 dark:text-blue-400" />
                    <BookOpen v-else-if="activity.type === 'grade'" class="h-5 w-5 text-green-600 dark:text-green-400" />
                    <DollarSign v-else-if="activity.type === 'payment'" class="h-5 w-5 text-purple-600 dark:text-purple-400" />
                    <Clock v-else class="h-5 w-5 text-orange-600 dark:text-orange-400" />
                  </div>
                  <div class="flex-1 space-y-1">
                    <p class="text-sm font-medium leading-none">{{ activity.action }}</p>
                    <p class="text-xs text-muted-foreground">{{ activity.user }}</p>
                  </div>
                  <span class="text-xs text-muted-foreground whitespace-nowrap">{{ activity.time }}</span>
                </div>
              </div>
            </CardContent>
          </Card>

          <!-- Right Sidebar -->
          <div class="col-span-3 space-y-4">
            <!-- Pending Tasks -->
            <Card>
              <CardHeader>
                <CardTitle>Pending Tasks</CardTitle>
                <CardDescription>Items requiring your attention</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-3">
                  <div v-for="task in pendingTasks" :key="task.id" class="flex items-start gap-3 p-3 rounded-lg border hover:bg-muted/50 transition-colors cursor-pointer">
                    <div :class="[
                      'flex h-8 w-8 items-center justify-center rounded-full mt-0.5',
                      task.priority === 'high' ? 'bg-red-100 dark:bg-red-900' : 
                      task.priority === 'medium' ? 'bg-yellow-100 dark:bg-yellow-900' : 
                      'bg-blue-100 dark:bg-blue-900'
                    ]">
                      <AlertCircle :class="[
                        'h-4 w-4',
                        task.priority === 'high' ? 'text-red-600 dark:text-red-400' : 
                        task.priority === 'medium' ? 'text-yellow-600 dark:text-yellow-400' : 
                        'text-blue-600 dark:text-blue-400'
                      ]" />
                    </div>
                    <div class="flex-1">
                      <p class="text-sm font-medium">{{ task.task }}</p>
                      <Badge :variant="task.priority === 'high' ? 'destructive' : task.priority === 'medium' ? 'default' : 'secondary'" class="mt-1.5">
                        {{ task.priority.toUpperCase() }}
                      </Badge>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

            <!-- Upcoming Events -->
            <Card>
              <CardHeader>
                <CardTitle>Upcoming Events</CardTitle>
                <CardDescription>Important dates this month</CardDescription>
              </CardHeader>
              <CardContent>
                <div class="space-y-3">
                  <div v-for="event in upcomingEvents" :key="event.id" class="flex items-start gap-3 p-3 rounded-lg border hover:bg-muted/50 transition-colors cursor-pointer">
                    <div class="flex h-12 w-12 flex-col items-center justify-center rounded-lg bg-primary/10 text-primary">
                      <span class="text-xs font-medium">NOV</span>
                      <span class="text-lg font-bold leading-none">{{ event.date.split(' ')[1].split('-')[0] }}</span>
                    </div>
                    <div class="flex-1">
                      <p class="text-sm font-medium">{{ event.title }}</p>
                      <p class="text-xs text-muted-foreground mt-1">{{ event.date }}</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>
          </div>
        </div>

        <!-- System Overview -->
        <div class="grid gap-4 md:grid-cols-3">
          <Card>
            <CardHeader>
              <CardTitle class="text-base">Student Overview</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Total Enrolled</span>
                  <span class="text-sm font-bold">1,284</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Grade 11</span>
                  <span class="text-sm font-bold">642</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Grade 12</span>
                  <span class="text-sm font-bold">642</span>
                </div>
                <div class="flex items-center justify-between pt-2 border-t">
                  <span class="text-sm text-muted-foreground">New This Month</span>
                  <span class="text-sm font-bold text-green-600">+24</span>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle class="text-base">Faculty Overview</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Total Teachers</span>
                  <span class="text-sm font-bold">87</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">On Duty Today</span>
                  <span class="text-sm font-bold">85</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">On Leave</span>
                  <span class="text-sm font-bold">2</span>
                </div>
                <div class="flex items-center justify-between pt-2 border-t">
                  <span class="text-sm text-muted-foreground">Pending Requests</span>
                  <span class="text-sm font-bold text-orange-600">5</span>
                </div>
              </div>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle class="text-base">Academic Overview</CardTitle>
            </CardHeader>
            <CardContent>
              <div class="space-y-3">
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Active Subjects</span>
                  <span class="text-sm font-bold">42</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Sections</span>
                  <span class="text-sm font-bold">24</span>
                </div>
                <div class="flex items-center justify-between">
                  <span class="text-sm text-muted-foreground">Avg. Class Size</span>
                  <span class="text-sm font-bold">53</span>
                </div>
                <div class="flex items-center justify-between pt-2 border-t">
                  <span class="text-sm text-muted-foreground">Avg. Performance</span>
                  <span class="text-sm font-bold text-green-600">87.5%</span>
                </div>
              </div>
            </CardContent>
          </Card>
        </div>

        <!-- Quick Actions -->
        <Card>
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
            <CardDescription>Frequently used administrative functions</CardDescription>
          </CardHeader>
          <CardContent>
            <div class="grid gap-3 md:grid-cols-2 lg:grid-cols-5">
              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10 hover:border-primary transition-colors">
                <Users class="h-6 w-6" />
                <span class="text-sm font-medium">Add Student</span>
              </Button>
              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10 hover:border-primary transition-colors">
                <GraduationCap class="h-6 w-6" />
                <span class="text-sm font-medium">Add Teacher</span>
              </Button>
              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10 hover:border-primary transition-colors">
                <BookOpen class="h-6 w-6" />
                <span class="text-sm font-medium">Create Subject</span>
              </Button>
              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10 hover:border-primary transition-colors">
                <Bell class="h-6 w-6" />
                <span class="text-sm font-medium">Post Announcement</span>
              </Button>
              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10 hover:border-primary transition-colors">
                <TrendingUp class="h-6 w-6" />
                <span class="text-sm font-medium">Generate Report</span>
              </Button>
            </div>
          </CardContent>
        </Card>
      </div>
    </SidebarInset>
  </SidebarProvider>
</template>