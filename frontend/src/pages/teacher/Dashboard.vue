<script lang="ts">
export const description = "Teacher dashboard overview"
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
  BookOpen,
  Calendar,
  Bell,
  UserCheck,
  PenLine,
  Users,
  CheckCircle,
  AlertCircle,
  ClipboardList,
} from "lucide-vue-next"

const userRole = "Teacher"

// Recent activity for TEACHERS
const recentActivities = [
  { id: 1, action: "Submitted grades for STEM 11-A", time: "10 minutes ago", type: "grade" },
  { id: 2, action: "Recorded attendance for HUMSS 12-B", time: "1 hour ago", type: "attendance" },
  { id: 3, action: "Checked 5 submitted assignments", time: "2 hours ago", type: "assignment" },
  { id: 4, action: "New announcement posted", time: "3 hours ago", type: "announcement" },
]

// Upcoming tasks specifically for Teachers
const teacherTasks = [
  { id: 1, task: "Grade 12 – Summative Test Checking", priority: "high" },
  { id: 2, task: "Upload Lesson Plan for Week 3", priority: "medium" },
  { id: 3, task: "Submit Class Attendance Summary", priority: "low" },
]

// Upcoming events
const upcomingEvents = [
  { id: 1, title: "Faculty Meeting", date: "Nov 18, 2025" },
  { id: 2, title: "Midterm Examination", date: "Nov 20-24, 2025" },
  { id: 3, title: "Campus Clean-up", date: "Dec 1, 2025" },
]
</script>

<template>
  <SidebarProvider>
    <AppSidebar :userRole="userRole" />

    <SidebarInset>
      <!-- Header -->
      <header class="flex h-16 shrink-0 items-center gap-2 transition-all">
        <div class="flex items-center gap-2 px-4">
          <SidebarTrigger class="-ml-1" />
          <Separator orientation="vertical" class="mr-2 h-4" />

          <Breadcrumb>
            <BreadcrumbList>
              <BreadcrumbItem class="hidden md:block">
                <BreadcrumbLink href="/teacher/dashboard">
                  Teacher
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

      <!-- Content -->
      <div class="flex flex-1 flex-col gap-4 p-4 pt-0">
        <!-- Welcome Card -->
        <div class="rounded-lg border bg-linear-to-r from-primary/10 via-primary/5 to-background p-6">
          <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
            <div>
              <h2 class="text-3xl font-bold">Welcome back, Teacher!</h2>
              <p class="text-muted-foreground mt-2">
                Saturday, November 15, 2025 • Your class updates for today.
              </p>
            </div>

            <div class="flex gap-2">
              <Button variant="outline">
                <Calendar class="mr-2 h-4 w-4" />
                My Schedule
              </Button>
              <Button>
                <ClipboardList class="mr-2 h-4 w-4" />
                Tasks
              </Button>
            </div>
          </div>
        </div>

        <!-- Quick Teaching Stats -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-4">
          <Card class="border-l-4 border-l-blue-500">
            <CardHeader class="flex justify-between items-center pb-2">
              <CardTitle class="text-sm font-medium">Classes Today</CardTitle>
              <BookOpen class="h-4 w-4 text-blue-600" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">5</div>
              <p class="text-xs text-muted-foreground mt-1">Across 3 grade levels</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-green-500">
            <CardHeader class="flex justify-between items-center pb-2">
              <CardTitle class="text-sm font-medium">Attendance Submitted</CardTitle>
              <UserCheck class="h-4 w-4 text-green-600" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">3 / 5</div>
              <p class="text-xs text-muted-foreground mt-1">2 classes remaining</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-yellow-500">
            <CardHeader class="flex justify-between items-center pb-2">
              <CardTitle class="text-sm font-medium">Pending Grading</CardTitle>
              <PenLine class="h-4 w-4 text-yellow-600" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">28</div>
              <p class="text-xs text-muted-foreground mt-1">Assignments to check</p>
            </CardContent>
          </Card>

          <Card class="border-l-4 border-l-purple-500">
            <CardHeader class="flex justify-between items-center pb-2">
              <CardTitle class="text-sm font-medium">Student Concerns</CardTitle>
              <AlertCircle class="h-4 w-4 text-purple-600" />
            </CardHeader>
            <CardContent>
              <div class="text-2xl font-bold">4</div>
              <p class="text-xs text-muted-foreground mt-1">Require follow-up</p>
            </CardContent>
          </Card>
        </div>

        <!-- Main Content -->
        <div class="grid gap-4 md:grid-cols-2 lg:grid-cols-7">
          
          <!-- Recent Activities -->
          <Card class="col-span-4">
            <CardHeader class="flex justify-between items-center">
              <div>
                <CardTitle>Recent Activities</CardTitle>
                <CardDescription>Updates from your classes</CardDescription>
              </div>
              <Button variant="ghost" size="sm">View All</Button>
            </CardHeader>

            <CardContent>
              <div class="space-y-3">
                <div
                  v-for="activity in recentActivities"
                  :key="activity.id"
                  class="flex items-center gap-4 p-3 rounded-lg border hover:bg-muted/50 transition cursor-pointer"
                >
                  <div
                    class="flex h-10 w-10 items-center justify-center rounded-full"
                    :class="{
                      'bg-green-100 dark:bg-green-900': activity.type === 'grade',
                      'bg-blue-100 dark:bg-blue-900': activity.type === 'attendance',
                      'bg-orange-100 dark:bg-orange-900': activity.type === 'assignment',
                      'bg-purple-100 dark:bg-purple-900': activity.type === 'announcement'
                    }"
                  >
                    <CheckCircle class="h-5 w-5 text-green-600" v-if="activity.type === 'grade'" />
                    <UserCheck class="h-5 w-5 text-blue-600" v-if="activity.type === 'attendance'" />
                    <PenLine class="h-5 w-5 text-orange-600" v-if="activity.type === 'assignment'" />
                    <Bell class="h-5 w-5 text-purple-600" v-if="activity.type === 'announcement'" />
                  </div>

                  <div class="flex-1">
                    <p class="text-sm font-medium">{{ activity.action }}</p>
                    <p class="text-xs text-muted-foreground">{{ activity.time }}</p>
                  </div>
                </div>
              </div>
            </CardContent>
          </Card>

          <!-- Right Sidebar -->
          <div class="col-span-3 space-y-4">
            
            <!-- Teacher Tasks -->
            <Card>
              <CardHeader>
                <CardTitle>Pending Tasks</CardTitle>
                <CardDescription>Your teaching-related tasks</CardDescription>
              </CardHeader>

              <CardContent>
                <div class="space-y-3">
                  <div
                    v-for="task in teacherTasks"
                    :key="task.id"
                    class="flex items-start gap-3 p-3 rounded-lg border hover:bg-muted/50 transition cursor-pointer"
                  >
                    <div :class="[
                      'flex h-8 w-8 items-center justify-center rounded-full mt-0.5',
                      task.priority === 'high' ? 'bg-red-100' :
                      task.priority === 'medium' ? 'bg-yellow-100' :
                      'bg-blue-100'
                    ]">
                      <AlertCircle class="h-4 w-4"
                        :class="[
                          task.priority === 'high' ? 'text-red-600' :
                          task.priority === 'medium' ? 'text-yellow-600' :
                          'text-blue-600'
                        ]"
                      />
                    </div>

                    <div class="flex-1">
                      <p class="text-sm font-medium">{{ task.task }}</p>
                      <Badge
                        class="mt-1.5"
                        :variant="
                          task.priority === 'high'
                            ? 'destructive'
                            : task.priority === 'medium'
                            ? 'default'
                            : 'secondary'
                        "
                      >
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
                <CardDescription>Stay updated with school activities</CardDescription>
              </CardHeader>

              <CardContent>
                <div class="space-y-3">
                  <div
                    v-for="ev in upcomingEvents"
                    :key="ev.id"
                    class="flex items-start gap-3 p-3 rounded-lg border hover:bg-muted/50 transition cursor-pointer"
                  >
                    <div class="flex h-12 w-12 items-center justify-center rounded-lg bg-primary/10 text-primary font-bold">
                      {{ ev.date.split(" ")[1] }}
                    </div>

                    <div class="flex-1">
                      <p class="text-sm font-medium">{{ ev.title }}</p>
                      <p class="text-xs text-muted-foreground mt-1">{{ ev.date }}</p>
                    </div>
                  </div>
                </div>
              </CardContent>
            </Card>

          </div>
        </div>

        <!-- Quick Actions -->
        <Card>
          <CardHeader>
            <CardTitle>Quick Actions</CardTitle>
            <CardDescription>Common tasks you frequently do</CardDescription>
          </CardHeader>

          <CardContent>
            <div class="grid gap-3 md:grid-cols-2 lg:grid-cols-5">
              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10">
                <ClipboardList class="h-6 w-6" />
                <span class="text-sm font-medium">Record Attendance</span>
              </Button>

              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10">
                <PenLine class="h-6 w-6" />
                <span class="text-sm font-medium">Submit Grades</span>
              </Button>

              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10">
                <BookOpen class="h-6 w-6" />
                <span class="text-sm font-medium">Upload Materials</span>
              </Button>

              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10">
                <Users class="h-6 w-6" />
                <span class="text-sm font-medium">View My Classes</span>
              </Button>

              <Button variant="outline" class="h-24 flex flex-col items-center justify-center gap-2 hover:bg-primary/10">
                <Bell class="h-6 w-6" />
                <span class="text-sm font-medium">Announcements</span>
              </Button>
            </div>
          </CardContent>
        </Card>

      </div>
    </SidebarInset>
  </SidebarProvider>
</template>
